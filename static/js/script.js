document.getElementById('authButton').addEventListener('click', function() {
  document.getElementById('authModal').classList.remove('hidden');
});

document.getElementById('sendCodeButton').addEventListener('click', function() {
  document.getElementById('authModal').classList.add('hidden');
  document.getElementById('codeModal').classList.remove('hidden');
});

document.getElementById('closeAuthModal').addEventListener('click', function() {
  document.getElementById('authModal').classList.add('hidden');
});

document.getElementById('closeCodeModal').addEventListener('click', function() {
  document.getElementById('codeModal').classList.add('hidden');
});
