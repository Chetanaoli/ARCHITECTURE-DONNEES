from activity2.activity21 import CustomGraph

def test_dfs(capsys):
    graph = CustomGraph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_link('A', 'B')
    graph.add_link('B', 'C')
    graph.add_link('C', 'D')

    graph.depth_first_search('A')

    captured = capsys.readouterr()
    expected_output = "A B C D "
    assert captured.out == expected_output

def test_dfs_with_disconnected_graph(capsys):
    graph = CustomGraph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_link('A', 'B')
    graph.add_link('C', 'D')


    graph.depth_first_search('A')

    captured = capsys.readouterr()
    expected_output = "A B "
    assert captured.out == expected_output
