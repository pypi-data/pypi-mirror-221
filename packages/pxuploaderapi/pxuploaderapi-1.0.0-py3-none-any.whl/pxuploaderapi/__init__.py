from uploader import Uploader
import pickle

class EcommerceUploaderAPI():
    def __init__(self, path):
        self.path = path
        # Get the uploader object from the path
        with open(self.path, "rb") as f:
            self.uploader = pickle.load(f)

    def getUploader(self) -> Uploader:
        return self.uploader
    
    def getTestOptions(self) -> dict:
        return self.getUploader().test_options.toDict()
    
    def getDeployOptions(self) -> dict:
        return self.getUploader().deploy_options.toDict()
    
    def getGithubOptions(self) -> dict:
        return self.getUploader().github_options.toDict()

        