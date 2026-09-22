from strands import Agent

# Bedrock is the default, so no model object is needed.
agent = Agent()
print(agent.state)
agent("What is an agent harness, in one sentence?")