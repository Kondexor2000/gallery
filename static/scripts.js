// Skrypt do potwierdzania usuwania zdjęcia
function confirmDelete(photoId) {
    if (confirm("Czy na pewno chcesz usunąć to zdjęcie?")) {
        window.location.href = `/delete_photo/${photoId}/`;
    }
}

// Skrypt do wyświetlania podglądu wybranego pliku
function previewImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var preview = document.getElementById('image-preview');
            preview.src = e.target.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(input.files[0]);
    }
}