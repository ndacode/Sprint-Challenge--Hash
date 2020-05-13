# One-Way Flight Trip

You've booked a _really_ cheap one-way flight. Unfortunately, that means
you have _tons_ of layovers before you reach your destination. The
morning of, you woke up late and had to scramble to the airport to catch
your first flight. However, in your rush, you accidentally scrambled all
your flight tickets. You don't know the route of your entire trip now!

Write a function

`reconstruct_trip` to reconstruct your trip from your
mass of flight tickets.

Each ticket is represented as a class with the

following form:

```
class Ticket:
    def __init__(self, source, destination):
        <!-- prev -->
        self.source = source
        <!-- next -->
        self.destination = destination
```

where the `source` string represents the starting airport and the
`destination` string represents the next airport along our trip.
The ticket for your first flight has a

<!-- self.source = None -->
<!-- this means the first item has a 'previous' of None -->

destination with a `source` of `NONE`,

<!-- self.destination = None -->

and the ticket for your final flight has a `source` with a
`destination` of `NONE`.

Pseudocode for an array of `Tickets` might look like this:

```
<!-- this looks like a dictionary -->
tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
]
```

Your function should output an array of strings with the entire route of
your trip. For the above example, it should look like this:

```
["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
```

Your solution should run in linear time. You can assume that your
function will always be handed a valid ticket chain as input.

## Hints

- The crux of this problem requires us to 'link' tickets together to
  reconstruct the entire trip. For example, if we have a ticket `('SJC', 'BOS')` that has us flying from San 
  Jose to Boston, then there exists
  another ticket where Boston is the starting location, `('BOS', 'JFK')`.
  <!-- so something like, "if self.destination isn't none and the hash table item's self.source == self.destination, add to linked list -->

- We can hash each ticket such that the starting location is the key and
  the destination is the value. Then, when constructing the entire
  route, the `i`th location in the route can be found by checking the
  <!-- index of current_location's previous location is current_location - 1 -->
  hash table for the `i-1`th location.
