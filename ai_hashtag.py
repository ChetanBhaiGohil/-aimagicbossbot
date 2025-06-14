def generate_hashtags(topic: str):
    topic = topic.lower().replace(" ", "_")
    return [f"#{topic}", f"#{topic}trend", f"#{topic}lovers", "#instagood", "#viral"]