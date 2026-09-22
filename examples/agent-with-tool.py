from strands import Agent
from strands_tools import generate_image, browser
# Bedrock is the default, so no model object is needed.
browser = LocalChromiumBrowser()
agent = Agent(tools=[generate_image, browser.browser ])

agent("Generate an image of a dog walking on the moon, and also show one pulled from the web")