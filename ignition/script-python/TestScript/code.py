# Project Library > TestScript - STATION-SPECIFIC UPDATE API

import system

logger = system.util.getLogger("myLogger_ProjectLibrary_hinge")
client = system.net.httpClient()

def handleTagChange(tag_value, description_tag_path):
    """Main function to handle tag changes and route to appropriate API calls"""
    """New change for testing git module"""
    logger.info("=== handleTagChange START ===")
    
    try:
        if isinstance(tag_value, basestring):
        	apiUrl = "http://localhost:5000/api/Parts?partNumberName={}".format(tag_value)
        	response = client.get(apiUrl)
        	logger.info("response-hinge: {}".format(response.getText()))
        	system.tag.writeBlocking([description_tag_path], [response.getText()])
        else:
            logger.info("Non-string tag value '{}' - ignoring".format(tag_value))
    except Exception as handle_error:
        logger.error("Error in handleTagChange: {}".format(str(handle_error)))
    logger.info("=== handleTagChange END ===")
