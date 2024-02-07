def order_queue(arr):
    seen_dict = {}

    # Count the number of times each person is seen
    for person in arr:
        if person not in seen_dict:
            seen_dict[person] = 0
        seen_dict[person] += 1

    # Sort the dictionary by the count of times each person is seen
    sorted_seen = sorted(seen_dict.items(), key=lambda x: x[1], reverse=True)

    # Reconstruct the queue based on the sorted dictionary
    ordered_queue = []
    for person, _ in sorted_seen:
        ordered_queue.extend([person] * seen_dict[person])

    return ordered_queue

# Test the function with an example input
input_queue = ["George Martin", "Mike Mendes", "Floyd Rose", "George Martin", "Mike Mendes", "Floyd Rose", "George Martin", "Mike Mendes", "Floyd Rose", "George Martin", "Mike Mendes", "Floyd Rose"]
ordered_queue = order_queue(input_queue)
print(ordered_queue)
