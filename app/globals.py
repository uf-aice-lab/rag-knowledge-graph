graph_index = None
graph_retriever = None


def set_graph_index(index):
    global graph_index
    global graph_retriever
    graph_index = index
    # Initialize the graph_retriever once the graph_index is set
    if graph_index is not None:
        print("Initializing graph retriever...")
        graph_retriever = graph_index.as_retriever(retriever_mode='hybrid')


def get_graph_index():
    return graph_index


def get_graph_retriever():
    return graph_retriever

