"""Flask Stack Simulator: Push, Pop, Peek, and Clear using a Stack class."""
import secrets

from flask import (Flask, flash, redirect, render_template, request,
                   session, url_for)

from stack_model import Stack

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

MAX_ITEMS = 20
MAX_REMOVED = 20
MAX_LENGTH = 24


@app.route('/')
def index():
    stack = Stack(session.get('stack', []))
    popped = session.get('popped', [])
    highlight = session.pop('peek', False)
    return render_template(
        'index.html',
        items=list(reversed(stack.items)),
        size=stack.size(),
        popped=list(reversed(popped)),
        highlight=highlight and not stack.is_empty(),
    )


@app.route('/stack', methods=['POST'])
def operate():
    action = request.form.get('action', '')
    value = request.form.get('value', '').strip()
    stack = Stack(session.get('stack', []))
    popped = list(session.get('popped', []))

    if action == 'push':
        if not value:
            flash('Enter a value before pushing.', 'error')
        elif len(value) > MAX_LENGTH:
            flash(f'Value must be {MAX_LENGTH} characters or fewer.', 'error')
        elif stack.size() >= MAX_ITEMS:
            flash(f'Stack is full ({MAX_ITEMS} items maximum).', 'error')
        else:
            stack.push(value)
            flash(f'Pushed "{value}" onto the stack.', 'success')
    elif action == 'pop':
        if stack.is_empty():
            flash('Stack is empty. Nothing to pop.', 'error')
        else:
            removed = stack.pop()
            popped.append(removed)
            popped = popped[-MAX_REMOVED:]
            flash(f'Popped "{removed}" from the top.', 'success')
    elif action == 'peek':
        if stack.is_empty():
            flash('Stack is empty. Nothing to peek.', 'error')
        else:
            session['peek'] = True
            flash(f'Top of the stack is "{stack.peek()}".', 'success')
    elif action == 'clear':
        stack.clear()
        popped = []
        flash('Stack and removed items cleared.', 'success')
    else:
        flash('Unknown action.', 'error')

    session['stack'] = stack.items
    session['popped'] = popped
    return redirect(url_for('index'))


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)