module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    sass: {
      options: {
        loadPath: [
          'django_boilerplate/static/bower_components/foundation/scss',
        ]
      },
      dist: {
        options: {
          style: 'expanded'
        },
        files: {
          'django_boilerplate/static/css/app.css': 'django_boilerplate/static/scss/app.scss'
        }
      }
    },

    watch: {
      scripts: {
        files: [
          'django_boilerplate/static/scss/**/*.scss',
        ],
        tasks: ['sass'],
        options: {
          spawn: false,
        },
      },
    },

    clean: ["django_boilerplate/static/css"]
  });

  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-clean');

  grunt.registerTask('build', ['clean', 'sass']);
  grunt.registerTask('default', ['watch']);
};