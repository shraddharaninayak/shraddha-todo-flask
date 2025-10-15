document.getElementById('todoForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    itemName: document.getElementById('itemName').value,
    itemDescription: document.getElementById('itemDescription').value
  };
  const res = await fetch('/submittodoitem', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify(payload)
  });
  const data = await res.json();
  alert('Result: ' + JSON.stringify(data));
});
