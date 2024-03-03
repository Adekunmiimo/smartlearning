document.addEventListener('DOMContentLoaded', function() {
    const listItems = document.querySelectorAll('.course-box ul li');
    const boxes = document.querySelectorAll('.course .box');

    listItems.forEach(item => {
        item.addEventListener('click', function() {
            // Remove active class from all list items
            listItems.forEach(li => {
                li.classList.remove('active');
            });

            // Add active class to the clicked list item
            this.classList.add('active');

            // Hide all boxes
            boxes.forEach(box => {
                box.style.display = 'none';
            });

            // Show the corresponding box
            const targetId = this.getAttribute('data-target');
            const targetBox = document.getElementById(targetId);
            if (targetBox) {
                targetBox.style.display = 'block';
            }
        });
    });
});
