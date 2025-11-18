#Q5
#output = 
# 18.0
# 15.0

#Q6
def make_notification(user, *messages, urgent=False):
    message_str = " ".join(messages)
    if urgent:
        return f"URGENT: {user} - {message_str}"
    return f"{user} - {message_str}"

print(make_notification("admin","Server down!", urgent=True))

#Q7
#SELECT name, email FROM users LIMIT 10
#SELECT * FROM logs WHERE level='error' LIMIT 5

#Q8
def log_action(actor, *actions, timestamp=None, **context):
    action_str = ", ".join(actions)
    context_parts = [f"{k}={v}" for k, v in context.items()]
    context_str = ", ".join(context_parts)
    return f"{actor}: {action_str} | {context_str}"

print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))