import os


class GCloudSync:

    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):
        command: str = (
                f"aws s3 sync {filename} s3://{gcp_bucket_url}/{filepath}/ "
            )
        os.system(command)
        
    def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):
         command: str = (
                f"aws s3 sync s3://{gcp_bucket_url}/{filename}/ {destination} "
            )

         os.system(command)