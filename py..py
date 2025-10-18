from collections import deque

# --- Stack Implementation (LIFO) ---
print("STACK (LIFO) with deque")
stack = deque()

# Push: add to the end
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushes:", list(stack))

# Pop: remove from the end
print("Popped item:", stack.pop())
print("Stack now:", list(stack))

# Peek and check
print("Top item:", stack[-1] if stack else None)
print("Is stack empty?", len(stack) == 0)

print("\n" + "-"*40 + "\n")

-------------------------------------------------

# --- Queue Implementation (FIFO) ---
print("QUEUE (FIFO) with deque")
queue = deque()

# Enqueue: add to the end
queue.append('1')
queue.append('2')
queue.append('3')
print("Queue after enqueues:", list(queue))

# Dequeue: remove from the beginning
print("Dequeued item:", queue.popleft())
print("Queue now:", list(queue))

# Peek and check
print("Front item:", queue[0] if queue else None)
print("Is queue empty?", len(queue) == 0)


✅ Output:

STACK (LIFO) with deque
Stack after pushes: ['A', 'B', 'C']
Popped item: C
Stack now: ['A', 'B']
Top item: B
Is stack empty? False

----------------------------------------

QUEUE (FIFO) with deque
Queue after enqueues: ['1', '2', '3']
Dequeued item: 1
Queue now: ['2', '3']
Front item: 2
Is queue empty? False

