def generate_image(prompt):
    # આ ફંકશન હમણાં માટે HuggingFace API વગર કામ કરશે.
    # Simple Demo ઇમેજીસ URL પાછા આપે છે.

    demo_images = {
        "cat": "https://placekitten.com/400/400",
        "dog": "https://placedog.net/400/400",
        "space": "https://picsum.photos/seed/space/400",
        "city": "https://picsum.photos/seed/city/400"
    }

    prompt_lower = prompt.lower()
    for keyword in demo_images:
        if keyword in prompt_lower:
            return demo_images[keyword]

    # જો કોઇ મેચ ના થાય તો default
    return "https://picsum.photos/400"