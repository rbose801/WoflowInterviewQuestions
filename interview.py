import requests

starting_node = "089ef556-dfff-4ff2-9733-654645be56fe"
gateway = "https://nodes-on-nodes-challenge.herokuapp.com/nodes/"

# example = [
#     {
#         "id": "ac0e9fe4-8de0-41e6-9656-b07b40194f47",
#         "child_node_ids": ["f1f509be-e589-479e-a2d8-04cddbddc154", "9e145221-5a5a-446b-abdd-8092ced6a6cf"]
#     },
#     {
#         "id": "59013ddb-d691-43c8-8274-7c87e1d739b4",
#         "child_node_ids": []
#     }
# ]


def get_distict_node_count(start_id):
    starting_node = requests.get(f'{gateway}{start_id}').json()[0]

    stack, result, uniqueList = [starting_node], [], set()
    freqsMap = {}

    while stack:
        curr = stack.pop()
        if curr:
            result.append(curr)
            uniqueList.add(curr['id'])
            for node in curr['child_node_ids']:
                nodeRequest = requests.get(f'{gateway}{node}').json()[0]
                if node not in freqsMap:
                    freqsMap[node] = 1
                else:
                    freqsMap[node] += 1
                stack.append(nodeRequest)

    return max(freqsMap, key=freqsMap.get), len(uniqueList), result,


print(get_distict_node_count(start_id=starting_node))
