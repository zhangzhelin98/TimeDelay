const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
let mediaRecorder;
let mediaStream;
let recordedChunks = [];

startButton.addEventListener('click', async () => {
    try {
        mediaStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
        mediaRecorder = new MediaRecorder(mediaStream);

        mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                recordedChunks.push(event.data);
            }
        };

        mediaRecorder.start();
        startButton.style.display = 'none';
        stopButton.style.display = 'block';

        // 将录制状态保存到本地存储//失败。。。
        localStorage.setItem('recording', 'true');
    } catch (error) {
        console.error('无法访问摄像头或麦克风：', error);
    }
});

stopButton.addEventListener('click', () => {
    if (mediaRecorder && mediaRecorder.state === 'recording') {
        mediaRecorder.stop();
        mediaStream.getTracks().forEach((track) => track.stop());

        // 创建一个 Blob 包含所有录制的数据
        const blob = new Blob(recordedChunks, { type: 'video/webm' });
        recordedChunks = [];

        // 使用 MediaRecorder 构造函数创建一个新的 MediaRecorder，设置 mimeType 为 'video/mp4'
        const mp4MediaRecorder = new MediaRecorder([], { mimeType: 'video/mp4' });

        // 添加录制数据
        mp4MediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                recordedChunks.push(event.data);
            }
        };

        mp4MediaRecorder.start();
        mp4MediaRecorder.stop();
        
        // 创建一个 Blob 包含所有录制的数据
        const mp4Blob = new Blob(recordedChunks, { type: 'video/mp4' });

        // 创建一个 FormData 对象，用于将视频数据发送到服务器，保存为mp4格式，命名为layer.participant.code.mp4
        const formData = new FormData();
        formData.append('video', mp4Blob, `${player.participant.code}.mp4`);

        // 使用 fetch API 将视频数据发送到服务器
        fetch('/save_video/', {
            method: 'POST',
            body: formData,
        }).then((response) => {
            if (response.ok) {
                console.log(`视频已保存到 "video" 文件夹中，文件名为 ${player.participant.code}.mp4`);
            } else {
                console.error('保存视频时出错');
            }
        });

        stopButton.style.display = 'none';

        // 清除本地存储中的录制状态
        localStorage.removeItem('recording');
    }
});

// 在页面加载时检查本地存储，如果正在录制，则继续录制
document.addEventListener('DOMContentLoaded', () => {
    const isRecording = localStorage.getItem('recording');
    if (isRecording === 'true') {
        // 继续录制逻辑...
    }
});


