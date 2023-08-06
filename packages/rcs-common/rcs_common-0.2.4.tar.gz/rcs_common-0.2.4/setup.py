import setuptools
setuptools.setup(
    name='rcs_common',
    version='0.2.4',
    description='Common directory of Airwayz Dev',
    url='https://bitbucket.org/airwayzdev/common',
    # project_urls = {
    #     "Bug Tracker": "https://bitbucket.org/airwayzdev/common/issues"
    # },
    packages=['common'],

    install_requires=['awz-server-api-test','awz_client_api_test','swagger-ui-bundle==0.0.9','clickclick','jsonschema','inflection','openapi-spec-validator==0.6.0',\
                    'numpy','pandas>=1.5.2',\
                    'python_dateutil>=2.8.2','pytz>=2022.6','requests>=2.28.1',\
                    'rtree>=1.0.1','scipy>=1.11.1',\
                    'Shapely>=1.8.5.post1'],
                    
    dependency_links=['https://test.pypi.org/simple/'])
