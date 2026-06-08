# Video 050 — Animation Prompts (VEO 3)

STAGE: Animation Prompts
STATUS: approved

## 1. Universal Prompt (Apply to all 200 clips by default)
*VEO 3 image-to-video mode reads the source image for visuals. Do NOT add visual descriptions to this prompt. Just copy and paste exactly as below.*

```text
Slow, steady cinematic push-in, smooth and tripod-stable. Soft natural ambient motion in the scene — fabric, hair, leaves, or steam responding gently to air. Warm golden-hour lighting, long soft shadows, lifted warm tones. vintage celluloid film aesthetic, rich warm cinematic color grading, preserve handcrafted storybook miniature style and smooth claymation feel, fine natural grain, soft halation around highlights, shallow depth of field. Serene, intimate, contemplative mood.

Audio: Diegetic environmental sound only — soft ambient sounds natural to this scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.
```

## 2. Fallback Protocol (Only if Universal Prompt fails on specific shots)
*Use these only if a clip gets distorted, face warping, or weird physics with the Universal Prompt.*

### Fallback A: Close-up / Window / Static Portrait
```text
Static medium shot, subtle micro-movements, preserve facial expression and posture. Figure sits quietly, slight natural breathing motion, hands still. Warm golden-hour lighting, long soft shadows, lifted warm tones. vintage celluloid film aesthetic, rich warm cinematic color grading, preserve handcrafted storybook miniature style and smooth claymation feel, fine natural grain, soft halation around highlights, shallow depth of field. Serene, intimate, contemplative mood.

Audio: Diegetic environmental sound only — distant birds, quiet ambient, faint fabric settle. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.
```

### Fallback B: Garden / Wide Walking Shots
```text
Slow gentle parallax dolly-in, foreground-background depth separation. Figure moves slowly through garden, natural weight and gait. Warm golden-hour lighting, long soft shadows, lifted warm tones. vintage celluloid film aesthetic, rich warm cinematic color grading, preserve handcrafted storybook miniature style and smooth claymation feel, fine natural grain, soft halation around highlights, shallow depth of field. Serene, intimate, contemplative mood.

Audio: Diegetic environmental sound only — birdsong from multiple directions, light wind through leaves, soft footsteps on grass. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.
```

### Fallback C: Grounded Detail / Highly Detailed Still Objects (e.g. the wooden box, close-up hands)
```text
Static medium shot, hold still, preserve all elements exactly as in source image. Natural ambient motion only — no magical effects, no added light, no particles. Warm golden-hour lighting, long soft shadows, lifted warm tones. vintage celluloid film aesthetic, rich warm cinematic color grading, preserve handcrafted storybook miniature style and smooth claymation feel, fine natural grain, soft halation around highlights, shallow depth of field. Serene, contemplative mood.

Audio: Diegetic environmental sound only — natural physical sounds matching the environment in the scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.
```

## 3. Workflow Checklist (VEO 3)
- [ ] Render 200 clips using VEO 3 with Image-to-Video mode.
- [ ] Clip duration: exactly 8 seconds.
- [ ] If any clip generates weird audio/music despite the prompt, strip audio using ffmpeg: `ffmpeg -i input.mp4 -an output_no_audio.mp4`
- [ ] During editing, use **Frame Bridging**: The last frame of clip A becomes the start frame of clip B to maintain smooth continuity.
- [ ] Overlay the official Suno generated song over the clips in the final timeline.
