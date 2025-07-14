from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState,Blog
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self,llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)


    def build_title_graph(self):

        self.graph
        self.blog_node_obj=BlogNode(self.llm)



        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("blog_generator",self.blog_node_obj.content_generation)

        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "blog_generator")
        self.graph.add_edge("blog_generator", END)

        return self.graph
    
    def setup_graph(self, usecase):
        if usecase == "topic":
            self.build_title_graph()

        return self.graph.compile()


##### Below code is for the langsmith langgraph studio

llm=GroqLLM().get_llm()

##get the graph

graph_builder=GraphBuilder(llm)
graph=graph_builder.build_title_graph().compile()