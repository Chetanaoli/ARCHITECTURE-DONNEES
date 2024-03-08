from activity2.activity20 import CustomGraph

def test_add_vertex():
    graph = CustomGraph()
    graph.add_node('A')
    graph.add_node('B')

    assert 'A' in graph.vertices_and_neighbors
    assert 'B' in graph.vertices_and_neighbors
    assert 'C' not in graph.vertices_and_neighbors

def test_add_edge():
    graph = CustomGraph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')

    graph.add_link('A', 'B')
    graph.add_link('B', 'C')

    assert 'B' in graph.vertices_and_neighbors['A']
    assert 'A' in graph.vertices_and_neighbors['B']
    assert 'C' in graph.vertices_and_neighbors['B']
    assert 'B' in graph.vertices_and_neighbors['C']
    assert 'A' not in graph.vertices_and_neighbors['C']

def test_display_graph(capsys):
    graph = CustomGraph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_link('A', 'B')

    graph.show_graph()

    captured = capsys.readouterr()
    expected_output = "A: ['B']\nB: ['A']\n"
    assert captured.out == expected_output
