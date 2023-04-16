import { Component, OnInit } from '@angular/core';
import { ResumeService } from './services/resume.service';
import { tap } from 'rxjs';

@Component({
  selector: 'app-resume',
  templateUrl: './resume.component.html',
  styleUrls: ['./resume.component.scss']
})
export class ResumeComponent implements OnInit {

  resume: string = "";
  videoUrl: string = "";

  constructor(private resumeService: ResumeService) {

  }

  ngOnInit(): void {

  }

  getResume(url: string) {
    const isYoutubeUrl = this.checkIsYoutubeUrl(url);

    if (!isYoutubeUrl) {
      return;
    }

    const idVideo = this.checkVideoId(url);

    if (!idVideo) {
      return;
    }

    this.resumeService.getResume(idVideo).pipe(
      tap(resume => {
        this.resume = resume;
        console.log(this.resume)
      })
    ).subscribe();

  }


  private checkVideoId(url: string): string | undefined {
    const regexVideoId = /(?:youtu\.be\/|v=)([a-zA-Z0-9_-]{11})/;

    return url.match(regexVideoId)?.[1];
  }

  private checkIsYoutubeUrl(url: string): boolean {
    const regexIsYoutube = /(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/|youtu\.be\/)/;

    return regexIsYoutube.test(url)
  }
}
