from src.states.blogstate import Blog,BlogState
from langchain_core.messages import SystemMessage

class BlogNode:
    def __init__(self, llm):   
        self.llm=llm
    
    def title_creation(self, state:BlogState):

        prompt = """ You are an expert blog content writer, use markdown formatting. Generate a title for a blog on {topic}. This title should be creative and SEO friendly."""
        system_message=prompt.format(topic=state["topic"])
        response=self.llm.invoke(system_message)
        return {"blog":{"title": response.content}}
    
    
    def content_generation(self, state:BlogState):

        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use markdown formatting. Generate a detailed blog content with the detailed breakdown for the  {topic}"""
            system_message=system_prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']['title'], "content":response.content}}