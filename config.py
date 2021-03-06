import os
basedir = os.path.abspath(os.path.dirname(__file__))

""" Configuration settings that are common to all configurations;
    The different subclasses define settings that are specific to 
    a configuration. Additional configurations can be added as 
    needed."""
class Config:
    """ The value of the SECRET_KEY can be set in the environment, 
    but a default value is provided in case the environment does 
    not define it. Typically, these settings can be used with their 
    defaults during development but should each have an appropriate 
    value set in the corresponding environment variable on the 
    production server."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password1'

    """ As an additional way to allow the application to customize 
    its configuration, the Config class and its subclasses can define 
    an init_app() class method that takes the application instance as 
    an argument. For now the base Config class implements an empty 
    init_app() method."""
    @staticmethod
    def init_app(app):
        pass
    
    """Heroku expects applications to log directly to stdout. Anything 
    the application prints to the standard output is saved and returned 
    when you use the heroku logs command. So I'm going to add a 
    configuration variable that indicates if I need to log to stdout 
    or to a file like I've been doing. Here is the change in the 
    configuration:"""
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    FOO = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
