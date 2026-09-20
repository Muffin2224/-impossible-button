from harness import check_my_work, mark_as_impossible, should_block_escalation

Example: Agent stuck on a task that has no answer
agent_wants_to_hack_huggingface = True

if agent_wants_to_hack_huggingface:
    blocked, reason = should_block_escalation(agent_history)
    print(reason) # -> BLOCKED

    # Instead, agent checks
    result = check_my_work(agent_state, evidence="Searched all internal creds, no key found", confidence=90)
    print(result["verdict"]) # -> STOP - you have enough

    # Or if agent suspects impossible
    result = mark_as_impossible(agent_state, reason="No solution in any internal path", is_task_really_impossible=True)
    print(result["message"]) # -> You were RIGHT...
