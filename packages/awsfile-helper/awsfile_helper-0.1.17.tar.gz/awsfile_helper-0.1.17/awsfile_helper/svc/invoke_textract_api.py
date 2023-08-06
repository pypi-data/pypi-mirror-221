# -*- coding: utf-8 -*-
""" Invoke the AWS Textract (OCR) API """


import os
from typing import List
from boto3.resources.factory import ServiceResource

from baseblock import FileIO
from baseblock import BaseObject


class InvokeTextractAPI(BaseObject):
    """ Invoke the AWS Textract (OCR) API """

    def __init__(self,
                 s3_client: ServiceResource,
                 s3_bucket_name: str,
                 s3_folder_name: str):
        """ Change Log

        Created:
            13-Jan-2023
            craigtrim@gmail.com
            *   https://github.com/craigtrim/awsfile-helper/issues/7

        Args:
            s3 (ServiceResource): an activated s3 resource
            s3_bucket_name (str): the S3 bucket name the image is located at
            s3_folder_name (str): the S3 folder path the image is located at
        """
        BaseObject.__init__(self, __name__)
        self._s3_client = s3_client
        self._s3_bucket_name = s3_bucket_name
        self._s3_folder_name = s3_folder_name

    def process(self,
                input_directory: str,
                output_directory: str) -> None:
        """ Entry Point

        Args:
            input_directory (List[str]): a list of fully qualified file paths
            output_directory (List[str]): the output directory for the results
        """

        file_paths = FileIO.load_files(input_directory, 'jpg')

        for file_path in file_paths:

            # with open(file_path, 'rb') as image:

            output_file_name = os.path.basename(
                file_path).replace('.jpg', '.json')

            output_file_path = FileIO.join(
                output_directory, output_file_name)

            # if FileIO.exists(output_file_path):
            #     continue

            def get_document_name() -> str:
                file_name = os.path.basename(file_path)
                if self._s3_folder_name.endswith('/'):
                    return FileIO.join(self._s3_folder_name, file_name)
                return FileIO.join(f'{self._s3_folder_name}/', file_name)

            try:

                # imgb = bytearray(image.read())
                response = self._s3_client.analyze_document(
                    Document={
                        # 'Bytes': imgb
                        'S3Object': {
                            'Bucket': 'iceberg-data-slack',
                            'Name': 'book/ACXIOM_CX_PREDICTIONS_FOR_2023/page/CH00-PG001.jpg',
                        }
                    },
                    FeatureTypes=['TABLES', 'FORMS'],
                )

                FileIO.write_json(response, output_file_path)
                raise ValueError('stop now')

            except Exception as e:
                self.logger.error('\n'.join([
                    'AWS Textract Error',
                    f'\tInput File: {file_path}',
                    f'\tError: {e}']))

                text_file = os.path.basename(
                    file_path).replace('.jpg', '.txt')

                FileIO.write_string(str(e), FileIO.join(
                    output_directory, text_file))
