module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    sass: {
      options: {
        loadPath: [
          'django_boilerplate/assets/bower_components/foundation/scss',
        ]
      },
      dist: {
        options: {
          style: 'compressed'
        },
        files: {
          'django_boilerplate/assets/build/css/app.css': 'django_boilerplate/assets/scss/app.scss'
        }
      }
    },

    watch: {
      scripts: {
        files: [
          'django_boilerplate/assets/scss/**/*.scss',
        ],
        tasks: ['sass'],
        options: {
          spawn: false,
        },
      },
    },

    copy: {
      main: {
        files: [
          {expand: true, cwd: 'django_boilerplate/assets/', src: ['images/**'], dest: 'django_boilerplate/assets/build/'},
          {expand: true, cwd: 'django_boilerplate/assets/', src: ['fonts/**'], dest: 'django_boilerplate/assets/build/'},
          {expand: true, cwd: 'django_boilerplate/assets/bower_components/modernizr', src: ['modernizr.js'], dest: 'django_boilerplate/assets/build/js/'},
        ],
      },
    },

    requirejs: {
      compile: {
        options: {
          baseUrl: 'django_boilerplate/assets/js',
          out: 'django_boilerplate/assets/build/js/app.js',
          name: '../bower_components/almond/almond',
          include: 'config',
          mainConfigFile: 'django_boilerplate/assets/js/config.js',
        }
      }
    },

    clean: ["django_boilerplate/assets/build"]
  });

  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-requirejs');

  grunt.registerTask('build', [
    'clean',
    'copy',
    'requirejs',
    'sass',
  ]);
  grunt.registerTask('default', ['watch']);
};