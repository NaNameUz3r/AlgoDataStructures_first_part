from queue import Queue


def spin_queue(queue_to_spin, steps_to_spin):

    for _ in range(steps_to_spin):
        queue_to_spin.enqueue(queue_to_spin.dequeue())
