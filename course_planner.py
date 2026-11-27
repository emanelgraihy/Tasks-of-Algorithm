from collections import deque, defaultdict


def plan_courses(courses: list[str], prerequisites: list[tuple[str, str]]):
    graph = defaultdict(list)
    in_degree = {course: 0 for course in courses}

    for pre, course in prerequisites:
        if pre not in in_degree:
            in_degree[pre] = 0
        if course not in in_degree:
            in_degree[course] = 0
        graph[pre].append(course)
        in_degree[course] += 1

    queue = deque([course for course, deg in in_degree.items() if deg == 0])
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for nxt in graph[current]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(order) != len(in_degree):
        remaining = [c for c, deg in in_degree.items() if deg > 0]
        return False, [], remaining

    return True, order, []


if __name__ == "__main__":
    courses_1 = ["CS101", "CS102", "CS201", "CS301"]
    prereqs_1 = [
        ("CS101", "CS102"),
        ("CS101", "CS201"),
        ("CS102", "CS301"),
        ("CS201", "CS301"),
    ]

    ok, course_order, cycle_nodes = plan_courses(courses_1, prereqs_1)
    print("Example 1:")
    if ok:
        print("Course order:", " -> ".join(course_order))
    else:
        print("Cycle detected:", cycle_nodes)

    courses_2 = ["MATH101", "MATH102", "PHYS101"]
    prereqs_2 = [
        ("MATH101", "MATH102"),
        ("MATH102", "PHYS101"),
        ("PHYS101", "MATH102"),
    ]

    ok2, course_order2, cycle_nodes2 = plan_courses(courses_2, prereqs_2)
    print("\nExample 2:")
    if ok2:
        print("Course order:", " -> ".join(course_order2))
    else:
        print("Cycle detected:", cycle_nodes2)