module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    sass: {
      options: {
        loadPath: [
          'static/bower_components/foundation/scss',
        ]
      },
      dist: {
        options: {
          style: 'expanded'
        },
        files: {
          'static/css/app.css': 'static/scss/app.scss'
        }
      }
    },

    watch: {
      scripts: {
        files: [
          'static/scss/**/*.scss',
        ],
        tasks: ['sass'],
        options: {
          spawn: false,
        },
      },
    },

    clean: ["static/css"]
  });

  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-clean');

  grunt.registerTask('build', ['clean', 'sass']);
  grunt.registerTask('default', ['watch']);
};