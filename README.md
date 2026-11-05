# F1 Stack Simulator

Name: Ezra Mae R. Tumanan

Section: BSIT WMT 4-2

Original starter repository: https://github.com/Jackson-Soriano/f1-elec4-stack-simulator-starter.git

Activity description: Bonus topic (Weeks 12-13). I completed the Flask Stack Simulator (LIFO) and created a separate Flask Queue Simulator (FIFO) in the `queue-simulator` folder.

---

# Flask Stack and Queue Simulators

## Stack Simulator (root folder)

Operations: Push, Pop, Peek, Clear (LIFO).

```
pip install -r requirements.txt
python app.py          # http://127.0.0.1:5000
```

## Queue Simulator (`queue-simulator/`)

Operations: Enqueue, Dequeue, Peek, Clear (FIFO). Front and Rear are labeled in the interface.

```
cd queue-simulator
pip install -r requirements.txt
python app.py          # http://127.0.0.1:5001
```

## Files

- `app.py`: Flask routes (`/`, `/stack` or `/queue`, `/contact`) using the session.
- `stack_model.py` / `queue_model.py`: the Stack and Queue classes (Python lists).
- `templates/`: `base.html` layout, `index.html` simulator, `contact.html` placeholder (Jinja2).
- `static/`: CSS and jQuery focus/peek effect.
