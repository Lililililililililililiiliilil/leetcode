messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
senders = ["Bob","Charlie"]

messages_count = {}

for i in range(len(senders)):
    if senders[i] not in messages_count:
        messages_count[senders[i]] = len(messages[i].split(" "))
    else:
        messages_count[senders[i]] += len(messages[i].split(" "))

possible_users = [k for k, v in messages_count.items() if v == max(messages_count.values())]
print(max(possible_users))

