# AWS File Helper (awsfile-helper)
Content Management and Retrieval for Cloud and Local Storage

## Code Usage (Authorization)
You must have an AWS Access Key and Secret Access key to connect to AWS.

Upon obtaining these keys, use
```python
from baseblock import CryptoBase

os.environ['AWS_ACCESS_KEY'] = CryptoBase().encrypt_str('<my-access-key>')
os.environ['AWS_SECRET_KEY'] = CryptoBase().encrypt_str('<my-secret-key>')
```

This will place your encrypted credentials into the environment.

The `AwsAPI` class will retrieve and decrypt these credentials to login.

## Code Usage (General)
The following code will retrieve any file:
```python
from awsfile_helper import FindOwlFile

d_cloud_file = FindS3File(
    file_name='config/graphviz/stylesheets/nlu',
    file_ext='yaml', file_version='0.1.0').process()
```
The bucket is assumed to be `data-core-bast`.

We can modify this assumption down the road if we create new buckets for different clients, etc.

A file may also be retrieved without a version, like this:
```python
d_cloud_file = FindS3File(
    file_name='config/graphviz/stylesheets/nlu',
    file_ext='yaml').process()
```

In that case, the system will first look in the environment, using a key configuration that relies on the `file_name` like this: `CONFIG_GRAPHVIZ_STYLESHEETS_NLU_VERSION`.  If no value is found in the environment, the system will consider this a _wildcard_ match and set the version to `*`.  This forces the system to list the contents of the qualified path and choose the latest version.  This operation takes an additional 2-3 milliseconds, assuming the network is running smoothly.


## Code Usage (Ontologies)
Ontologies require a special finder class, because we typically have two files we want to retrieve - an OWL model and a TXT file with synonyms.

Therefore, assume that an S3 bucket exists with two files we want to retrieve: `syllabus.owl` and `syllabus.txt`.

The following code will retrieve these files:
```python
from awsfile_helper import FindOwlFile

d_cloud_file = FindOwlFile(file_name='syllabus', version='0.1.0').process()
```

Note that we did not specify the file extension within the `file_name` variable.

It is permissible to specify explicit file names such as `syllabus.txt` or partial file names such.

The result dictionary is keyed by file name and (with redacted contents) looks like this:
```json
{
    "owl": {
        "path": "<local path to OWL file">,
        "version": "<version of OWL file>",
        "contents": "<contents of OWL file>"
    },
    "txt": {
        "path": "<local path to txt file">,
        "version": "<version of txt file>",
        "contents": "<contents of txt file>"
    }
}
```
