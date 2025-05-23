import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly username = 'admin';
  private readonly password = 'admin';
  private isLoggedIn = false;

  login(user: string, pass: string): boolean {
    if (user === this.username && pass === this.password) {
      this.isLoggedIn = true;
      return true;
    }
    return false;
  }

  logout(): void {
    this.isLoggedIn = false;
  }

  isAuthenticated(): boolean {
    return this.isLoggedIn;
  }
}