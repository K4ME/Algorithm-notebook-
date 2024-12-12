## Stacks
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.  
This means that the last element added to the stack is the first one to be removed.  
**It can be visualized as a pile of plates where you can only add or remove the top plate.**  

### Operations on Stack:
The primary operations associated with a stack are:

**Push:** Adds an element to the top of the stack.  
**Pop:** Removes and returns the top element of the stack.  
**Peek (or Top):** Returns the top element of the stack without removing it.  
**IsEmpty:** Checks if the stack is empty.  
**Size:** Returns the number of elements in the stack.  

### Use Cases of Stack:  
Stacks are used in various applications, including:  

**Function Call Management:** The call stack in programming languages keeps track of function calls and returns.  
**Expression Evaluation:** Used in parsing expressions and evaluating postfix or prefix notations.  
**Backtracking:** Helps in algorithms that require exploring all possibilities, such as maze solving and depth-first search.  


## Queues
A queue is a linear data structure that follows the First In, First Out (FIFO) principle.  
This means that the first element added to the queue is the first one to be removed.  
**It can be visualized as a line of people waiting for a service, where the first person in line is the first to be served.**  

### Operations on Queue:  
The primary operations associated with a queue are:  

**Enqueue:** Adds an element to the end (rear) of the queue.  
**Dequeue:** Removes and returns the front element of the queue.  
**Front (or Peek):** Returns the front element of the queue without removing it.  
**IsEmpty:** Checks if the queue is empty.  
**Size:** Returns the number of elements in the queue.  

### Use Cases of Queue:  
Queues are used in various applications, including: 

**Task Scheduling:** Operating systems use queues to manage tasks and processes.  
**Breadth-First Search (BFS):** In graph traversal algorithms, queues help in exploring nodes level by level.  
**Buffering:** Used in situations where data is transferred asynchronously, such as IO buffers and print spooling.  

  
## Key Differences Between Stack and Queue

<table>
<thead>
<tr>
<th><span>Feature</span></th>
<th><span>Stack</span></th>
<th><span>Queue</span></th>
</tr>
</thead>
<tbody>
<tr>
<th><b><strong>Definition</strong></b></th>
<td><span>A linear data structure that follows the</span><b><strong> Last In First Out (LIFO) </strong></b><span>principle.</span></td>
<td><span>A linear data structure that follows the</span><b><strong> First In First Out (FIFO)</strong></b><span> principle.</span></td>
</tr>
<tr>
<th><b><strong>Primary Operations</strong></b></th>
<td><span>Push (add an item), Pop (remove an item), Peek (view the top item)</span></td>
<td><span>Enqueue (add an item), Dequeue (remove an item), Front (view the first item), Rear (view the last item)</span></td>
</tr>
<tr>
<th><b><strong>Insertion/Removal</strong></b></th>
<td><span>Elements are added and removed from the same end (the top).</span></td>
<td><span>Elements are added at the rear and removed from the front.</span></td>
</tr>
<tr>
<th><b><strong>Use Cases</strong></b></th>
<td><span>Function call management (call stack), expression evaluation and syntax parsing, undo mechanisms in text editors.</span></td>
<td><span>Scheduling processes in operating systems, managing requests in a printer queue, breadth-first search in graphs.</span></td>
</tr>
<tr>
<th><b><strong>Examples</strong></b></th>
<td><span>Browser history (back button), reversing a word.</span></td>
<td><span>Customer service lines, CPU task scheduling.</span></td>
</tr>
<tr>
<th><b><strong>Real-World Analogy</strong></b></th>
<td><span>A stack of plates: you add and remove plates from the top.</span></td>
<td><span>A queue at a ticket counter: the first person in line is the first to be served.</span></td>
</tr>
<tr>
<th><b><strong>Complexity (Amortized)</strong></b></th>
<td><b><strong>Push: </strong></b><span>O(1), </span><b><strong>Pop:</strong></b><span> O(1),</span><b><strong> Peek: </strong></b><span>O(1)</span></td>
<td><b><strong>Enqueue: </strong></b><span>O(1), </span><b><strong>Dequeue:</strong></b><span> O(1), </span><b><strong>Front: </strong></b><span>O(1), </span><b><strong>Rear:</strong></b><span> O(1)</span></td>
</tr>
<tr>
<th><b><strong>Memory Structure</strong></b></th>
<td><span>Typically uses a contiguous block of memory or linked list.</span></td>
<td><span>Typically uses a circular buffer or linked list.</span></td>
</tr>
<tr>
<th><b><strong>Implementation</strong></b></th>
<td><span>Can be implemented using arrays or linked lists.</span></td>
<td><span>Can be implemented using arrays, linked lists, or circular buffers.</span></td>
</tr>
</tbody>
</table>
