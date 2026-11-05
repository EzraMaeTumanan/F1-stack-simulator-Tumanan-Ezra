"""Flask Queue Simulator: Enqueue, Dequeue, Peek, and Clear using a Queue class."""
import secrets

from flask import (Flask, flash, redirect, render_template, request,
                   session, url_for)

from queue_model import Queue

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
# Separate cookie name so this app does not clash with the stack simulator on localhost.
app.config['SESSION_COOKIE_NAME'] = 'queue_session'

MAX_ITEMS = 20
MAX_REMOVED = 20
MAX_LENGTH = 24


@app.route('/')
def index():
    queue = Queue(session.get('queue', []))
    removed = session.get('removed', [])
    highlight = session.pop('peek', False)   # One-time flag set by Peek.
    return render_template(
        'index.html',
        items=queue.items,                   # Front first, rear last (no reversing).
        size=queue.size(),
        removed=list(reversed(removed)),     # Most recently removed first.
        highlight=highlight and not queue.is_empty(),
    )


@app.route('/queue', methods=['POST'])
def operate():
    action = request.form.get('action', '')
    value = request.form.get('value', '').strip()
    queue = Queue(session.get('queue', []))
    removed = list(session.get('removed', []))

    if action == 'enqueue':
        if not value:
            flash('Enter a value before enqueueing.', 'error')
        elif len(value) > MAX_LENGTH:
            flash(f'Value must be {MAX_LENGTH} characters or fewer.', 'error')
        elif queue.size() >= MAX_ITEMS:
            flash(f'Queue is full ({MAX_ITEMS} items maximum).', 'error')
        else:
            queue.enqueue(value)
            flash(f'Enqueued "{value}" at the rear.', 'success')
    elif action == 'dequeue':
        if queue.is_empty():
            flash('Queue is empty. Nothing to dequeue.', 'error')
        else:
            front = queue.dequeue()
            removed.append(front)
            removed = removed[-MAX_REMOVED:]
            flash(f'Dequeued "{front}" from the front.', 'success')
    elif action == 'peek':
        if queue.is_empty():
            flash('Queue is empty. Nothing to peek.', 'error')
        else:
            session['peek'] = True
            flash(f'Front of the queue is "{queue.peek()}".', 'success')
    elif action == 'clear':
        queue.clear()
        removed = []
        flash('Queue and removed items cleared.', 'success')
    else:
        flash('Unknown action.', 'error')

    session['queue'] = queue.items
    session['removed'] = removed
    return redirect(url_for('index'))


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Port 5001 so both apps can run together.
