import os
import audio
import head_pose
import detection
import graph
import threading as th

if __name__ == "__main__":
    head_pose_thread = th.Thread(target=head_pose.pose)
    audio_thread = th.Thread(target=audio.sound)
    detection_thread = th.Thread(target=detection.run_detection)
    graph_thread = th.Thread(target=graph.run_graph)

    head_pose_thread.start()
    audio_thread.start()
    detection_thread.start()
    graph_thread.start()

    head_pose_thread.join()
    audio_thread.join()
    detection_thread.join()
    graph_thread.join()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
