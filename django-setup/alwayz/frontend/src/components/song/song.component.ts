import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../services/auth.service";
import {Router} from "@angular/router";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-song',
  templateUrl: './song.component.html',
  styleUrls: ['./song.component.css']
})
export class SongComponent implements OnInit {
  songs: any;
  ran: any;

  constructor(private authService: AuthService, private router: Router, private http: HttpClient) { }

  ngOnInit() {
    this.http.get('./../assets/songs.json').subscribe((data)=>{
      this.songs = data['songs'];
      console.log(this.songs);
      this.ran = this.songs[Math.floor(Math.random() * this.songs.length)];
    })
  }

  liked(){

  }

  logout(){
    this.authService.logout();
    this.router.navigate(['login']);
  }
}
