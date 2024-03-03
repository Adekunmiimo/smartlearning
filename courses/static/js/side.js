<!-- Place this script tag at the bottom of your video_list.html -->

<script>
document.addEventListener('DOMContentLoaded', (event) => {
    const videos = document.querySelectorAll('.video-item');

    videos.forEach(video => {
        video.addEventListener('click', () => {
            alert(`You clicked on the video: ${video.querySelector('h2').textContent}`);
        });
    });
});
</script>
