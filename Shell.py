import os

class Shell:

    def StartLaravel(self, title, hasGit):
        if(bool(hasGit)):
            os.system(f"composer create-project laravel/laravel {title} --git")
        else:
            os.system(f"composer create-project laravel/laravel {title}")

        return True