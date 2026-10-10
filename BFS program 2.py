BFS(Graph, Start)
1. Create an empty visited set.
2. Create a queue and insert Start node.
3. While the queue is not empty:
      a. Remove the first node from the queue.
      b. If the node is not visited:
            i. Print the node.
            ii. Add the node to visited.
            iii. For each neighbor of the node:
                    If neighbor is not visited:
                        Add neighbor to queue.
4. Stop.
