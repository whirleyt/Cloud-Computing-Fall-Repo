import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostLikesComponent } from './post-likes.component';

describe('PostLikesComponent', () => {
  let component: PostLikesComponent;
  let fixture: ComponentFixture<PostLikesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PostLikesComponent]
    });
    fixture = TestBed.createComponent(PostLikesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
