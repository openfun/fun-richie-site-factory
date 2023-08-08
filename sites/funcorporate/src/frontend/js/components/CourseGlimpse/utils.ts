import { Course } from 'richie-education/js/types/Course';
import { CourseGlimpseCourse } from '.';

// FIXME: This is a partial implementation of the original function
// that is enough for the current use case of the FUN Corporate website and that allows
// to fix a regression introduced by the upgrade to Richie 2.23.0.
// This should be removed once the FUN Corporate website is upgraded to the next Richie version.

export const getCourseGlimpseProps = (course: Course): CourseGlimpseCourse => ({
  id: course.id,
  code: course.code,
  course_url: course.absolute_url,
  cover_image: course.cover_image,
  title: course.title,
  organization: {
    title: course.organization_highlighted,
    image: course.organization_highlighted_cover_image,
  },
  icon: course.icon,
  state: course.state,
  organizations: course.organizations,
  duration: course.duration,
  effort: course.effort,
});
