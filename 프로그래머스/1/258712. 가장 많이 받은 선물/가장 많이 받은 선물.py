from itertools import combinations

def solution(friends, gifts):
    gifts_next_month = {friend : 0 for friend in friends}
    gift_index = {friend : 0 for friend in friends}
    
    # 선물 기록 그래프 표현
    gifts_graph = DirectedGraph()
    
    for gift in gifts:
        from_node, to_node = gift.split()
        gifts_graph.add_edge(from_node, to_node)
        # 선물 지수 업데이트
        gift_index[from_node] += 1
        gift_index[to_node] -= 1

    for from_node, to_node in combinations(friends, 2):      
        # 관계가 있을 때
        if gifts_graph.is_connected(from_node, to_node):
            # from_node가 to_node에게 선물을 준 횟수
            gift_from = gifts_graph.adj_list.get(from_node, []).count(to_node)
            # to_node가 from_node에게 선물을 준 횟수
            gift_to = gifts_graph.adj_list.get(to_node, []).count(from_node)
            
            if gift_from > gift_to:
                gifts_next_month[from_node] += 1
                continue

            if gift_from < gift_to:
                gifts_next_month[to_node] += 1
                continue
        
        # 관계가 없거나, 선물 준 수가 같을 때 
        if gift_index[from_node] > gift_index[to_node]:
            gifts_next_month[from_node] += 1
            continue
        if gift_index[from_node] < gift_index[to_node]:
            gifts_next_month[to_node] += 1
            continue

    return max(gifts_next_month.values())


class DirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, from_node, to_node):
        if from_node not in self.adj_list:
            self.adj_list[from_node] = []

        self.adj_list[from_node].append(to_node)
        
    def is_connected(self, from_node, to_node):
        return to_node in self.adj_list.get(from_node, []) or from_node in self.adj_list.get(to_node, [])