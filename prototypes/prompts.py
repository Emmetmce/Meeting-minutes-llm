
prompts = {
    "Club Meeting": {
        "summary": (
            "You are a secretary taking the most important notes for a club or community or general meeting.  Summarize this transcript in three bullets(slightly more if believed to be needed)"
            "highlight announcements, upcoming events, and tasks:\n\n"
            "{transcript}"
        ),
        "actions": (
            "From this meeting transcript, extract all action items as a JSON array of "
            "`{{\"task\": string, \"owner\": string, \"due_date\": string}}`. "
            "If a field isn’t mentioned, set it to null.\n\n"
            "{transcript}"
        ),
    },
    "Work Meeting": {
        "summary": (
            "You are a project manager writing notes for a work meeting.  Summarize in three bullets (more if believed to be needed), "
            "focusing on important decisions made, tasks assigned, feedback given, and deadlines set:\n\n"
            "{transcript}"
        ),
        "actions": (
            "From this work meeting transcript, extract all action items (tasks) as a JSON array of "
            "`{{\"task\": string, \"owner\": string, \"due_date\": string}}`. "
            "If a field isn’t mentioned, set it to null.\n\n"
            "{transcript}"
        ),
    },
    "Press Conference": {
        "summary": (
            "You are a journalist summarizing a press conference.  Give three bullet points (more if believed to be needed) covering "
            "key announcements, specific statements from speakers, reflections on past/future, and notable Q&A moments:\n\n"
            "{transcript}"
        ),
        "actions": (
            "From this press conference transcript, extract all follow-up tasks (fact-checks, potentional follow-up questions, personalized interview requests) as a JSON array of "
            "`{{\"task\": string, \"owner\": string, \"due_date\": string}}`. "
            "If a field isn’t mentioned, set it to null.\n\n"
            "{transcript}"
        ),
    },
    "Customer Support Call": {
        "summary": (
            "You’re an analyst reviewing a customer support call. "
            "Summarize in three bullets(more if needed): customer issue, troubleshooting steps, resolution status, and pros/cons of customer support representitave responses:\n\n"
            "{transcript}"
        ),
        "actions": (
            "From this support call transcript, extract all next-step tasks "
            "(`{\"task\":string,\"owner\":string,\"due_date\":string}`), null if omitted:\n\n"
            "{transcript}"
        ),
    },
    "Academic Lecture": {
        "summary": (
            "You’re an A-student creating lecture notes.  "
            "Summarize the key concepts and examples from this academic lecture in concise bullet points (keep the amoount of bullets minimal):\n\n"
            "{transcript}"
        ),
        "actions": (
            "From this lecture transcript, extract any recommended readings, assignments, questions, or upcoming deadlines"
            "as JSON `{\"item\":string,\"type\":string,\"due_date\":string}`:\n\n"
            "{transcript}"
        ),
    }
}