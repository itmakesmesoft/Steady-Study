# 깊이우선탐색(DFS)

### 깊이 우선 탐색(DFS, Depth First Search)

- 루트 노드에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
- 그래프 탐색의 경우 어떤 노드를 방문했었는지를 반드시 검사해야 함
- 스택이나, 재귀를 이용하여 구현

### 깊이 우선 탐색(DFS)의 과정

1. a 노드(시작 노드)를 방문하고, 방문한 노드는 방문했다고 표시
2. a와 인접한 노드들을 차례로 순회. a와 인접한 노드가 없다면 종료.
3. a와 이웃한 노드 b를 방문했다면, a와 인접한 또 다른 노드를 방문하기 전에 b의 이웃 노드들을 전부 방문해야 함.
b를 시작 정점으로 DFS를 다시 시작하여 b의 이웃 노드들을 방문.
4. b의 분기를 전부 완벽하게 탐색했다면 다시 a에 인접한 정점들 중에서 아직 방문이 안 된 정점을 찾음. 즉, b의 분기를 전부 완벽하게 탐색한 뒤에야 a의 다른 이웃 노드를 방문할 수 있다는 의미.
방문이 안 된 정점이 있으면 그 정점으로 DFS를 시작, 없으면 종료

![[https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html](https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html)](./img/120.png)

[https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html](https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html)

### 깊이 우선 탐색(DFS)의 시간 복잡도

- DFS는 그래프의 모든 간선을 조회
    - 인접 리스트로 표현된 그래프 : O(n+e)
    - 인접 행렬로 표현된 그래프: O(n^2)
    

> **Reference**
> 

[[알고리즘] 깊이 우선 탐색(DFS)이란 - Heee's Development Blog](https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html)