window.onload = () => {
    const video  = document.getElementById("camera");
    const canvas = document.getElementById("photo");

    // カメラ設定
    const constraints = {
        audio: false,
        video: {
            width: 1920,
            height: 1080
        }
    };

    // 写真の解像度を設定
    canvas.width = constraints.video.width;
    canvas.height = constraints.video.height;

    // カメラに写っているものを <video> に流す
    navigator.mediaDevices.getUserMedia(constraints)
        .then( (stream) => {
            video.srcObject = stream;
            video.onloadedmetadata = (e) => {
                video.play();
            };
        })
        .catch( (err) => {
            console.error(err.name + ": " + err.message);
        });

    // シャッターボタン押下で発火
    document.getElementById("shutter").addEventListener("click", () => {
        
        // canvasに画像を貼り付ける
        const ctx = canvas.getContext("2d");
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);    // この瞬間にシャッターが切られる

        // canvas画像をBASE64形式に変換
//        const quality = 0.99;    // これ以上品質を上げると 1MB を超えてしまうかも
        const quality = 0.95;
        const photodata = canvas.toDataURL("image/jpeg", quality);
        console.log(photodata);

        // BASE64形式の写真データを liveSend する
        // 一発の liveSend のサイズが 1MB を超えると oTree は受け付けない？
        liveSend({
            "photostr": photodata
        });
    });
};
  
