from xray_vision.qt_widgets import CrossSectionMainWindow as main
m = main()
m.show()

# then you can do things like:
# m._messenger._view.update_image(np.random.random((100,100)))
# to update the cross section viewer