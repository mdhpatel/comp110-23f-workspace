"""Node Class."""

from __future__ import annotations

__author__ = 730710742


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return the data type for the first node in the list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Returns the list of nodes overall."""
        return self.next
    
    def last(self) -> int | None:
        """Returns the data type for the last node in the recursive list."""
        if self.next is None:
            return self.data
        else:
            return self.next.last()