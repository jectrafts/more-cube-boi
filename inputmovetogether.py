from twophase import solver as tw
import numpy as np
from twophase import solver as tw
import matplotlib.pyplot as plt
from matplotlib import widgets
from projection import Quaternion, project_points
import time

# white = ['yellow', 'red', 'blue', 'white', 'white', 'red', 'yellow', 'yellow', 'red']
# yellow = ['yellow', 'blue', 'red', 'blue', 'yellow', 'blue', 'red', 'green', 'white']
# red = ['blue', 'orange', 'blue', 'orange', 'red', 'red', 'red', 'yellow', 'blue']
# orange= ['white', 'yellow', 'green', 'orange', 'orange', 'green', 'orange', 'yellow', 'green']
# green = ['orange', 'green', 'orange', 'orange', 'green', 'blue', 'white', 'red', 'green']
# blue = ['white', 'white', 'orange', 'green', 'blue', 'white', 'yellow', 'white', 'green']

white = ['white', 'yellow', 'yellow', 'yellow', 'white', 'red', 'white', 'blue', 'white']
yellow = ['yellow', 'white', 'green', 'white', 'yellow', 'green', 'green', 'yellow', 'red']
red = ['orange', 'orange', 'red', 'white', 'red', 'red', 'green', 'blue', 'orange']
orange= ['blue', 'blue', 'green', 'blue', 'orange', 'white', 'yellow', 'green', 'red']
green = ['red', 'orange', 'blue', 'red', 'green', 'green', 'yellow', 'orange', 'orange']
blue = ['blue', 'green', 'orange', 'yellow', 'blue', 'red', 'white', 'orange', 'blue']





faces = [white, blue, red, yellow, green, orange]

# Create color map based on center stickers
color_map = {
    'white': 'U',   # white center
    'blue': 'R',    # blue center
    'red': 'F',     # red center
    'yellow': 'D',  # yellow center
    'green': 'L',   # green center
    'orange': 'B'   # orange center
}

# Convert to 54-letter cube string
cube_str = ''.join(color_map[color] for face in faces for color in face)

# Solve
solution = tw.solve(cube_str)

# Output
print("Cube string:", cube_str)
print("Solution:", solution)
print(len(solution))
#----------------------------------------------------------------------
# Matplotlib Rubik's cube simulator
# Written by Jake Vanderplas
# Adapted from cube code written by David Hogg
#   https://github.com/davidwhogg/MagicCube
wooo=0
ropes=['blue', 'white', 'green', 'red', 'white', 'yellow', 'white', 'red', 'orange']

# white =['yellow', 'red', 'white', 'yellow', 'white', 'red', 'green', 'white', 'blue']
# yellow= ['red' ,'white', 'red', 'red', 'yellow', 'white', 'red' ,'yellow', 'orange']
# red =['white', 'red', 'yellow', 'blue', 'red', 'orange', 'yellow', 'blue', 'yellow']
# orange= ['green', 'yellow', 'green', 'white', 'orange', 'orange', 'white', 'green', 'white']
# green =['orange', 'orange', 'red', 'green', 'green', 'yellow', 'blue', 'green', 'blue']
# blue =['orange', 'blue', 'orange', 'blue', 'blue', 'green', 'green', 'orange', 'blue']

faces = [white, blue, red, yellow, green, orange]
abc =1
color_map = {
    white[4]: 'U',   # white center
    blue[4]: 'R',    # blue center
    red[4]: 'F',     # red center
    yellow[4]: 'D',  # yellow center
    green[4]: 'L',   # green center
    orange[4]: 'B'   # orange center
}

# Convert to 54-letter cube string
cube_str = ''.join(color_map[color] for face in faces for color in face)

# Solve
solution = tw.solve(cube_str)

# Output
print("Cube string:", cube_str)
print("Solution:", solution)
solution = solution[:-5]
pr = str(solution)
color_to_hex = {
    'white': "#ffffff",  # or "w" if you really want a symbol
    'yellow': "#ffcf00",
    'blue': "#00008f",
    'green': "#009f0f",
    'orange': "#ff6f00",
    'red': "#cf0000"
}
whiteh= [color_to_hex[color] for color in white]
yellowh= [color_to_hex[c] for c in yellow]
redh= [color_to_hex[color2] for color2 in red]
orangeh= [color_to_hex[color3] for color3 in orange]
greenh= [color_to_hex[color4] for color4 in green]
blueh= [color_to_hex[color5] for color5 in blue]

orangeh[5],orangeh[4],orangeh[8],orangeh[3],orangeh[2],orangeh[7],orangeh[1],orangeh[0],orangeh[6] =orangeh[0],orangeh[1],orangeh[2],orangeh[3],orangeh[4],orangeh[5],orangeh[6],orangeh[7],orangeh[8]

blueh,greenh=greenh,blueh
def transpose_and_flatten(arr):
    size = 3  # 3x3 grid
    grid = [arr[i:i+size] for i in range(0, len(arr), size)]
    transposed = list(zip(*grid))  # Transpose
    return [item for row in transposed for item in row]  # Flatten




blueh = transpose_and_flatten(blueh)
greenh = transpose_and_flatten(greenh)

def parse_moves(pr):
    z = []  # faces
    f = []  # counts
    i = 0
    while i < len(pr):
        if pr[i] == ' ':
            i += 1
            continue
        z.append(pr[i])
        f.append(int(pr[i + 1]))
        i += 3
    return list(zip(z, f))

def _play_moves(self, event):
    pr = "U2 R2 F1 L1 F2 B2 L2 F3 L1 F1 B2 U2 B2 L2 B2 L2 D1 F2 U1 F2"
    moves = parse_moves(pr)
    for face, count in moves:
        self.rotate_face(face, count)
        color_map = {
        white[4]: 'U',   # white center
        blue[4]: 'R',    # blue center
        red[4]: 'F',     # red center
        yellow[4]: 'D',  # yellow center
        green[4]: 'L',   # green center
        orange[4]: 'B'   # orange center
    }

    # Convert to 54-letter cube string
    cube_str = ''.join(color_map[color] for face in faces for color in face)

    # Solve
    solution = tw.solve(cube_str)

    # Output
    print("Cube string:", cube_str)
    print("Solution:", solution)
    solution = solution[:-5]
    pr = str(solution)



def rotate_90_right(arr):
    size = 3  # 3x3 grid
    grid = [arr[i:i+size] for i in range(0, len(arr), size)]
    rotated = list(zip(*grid[::-1]))  # Transpose + reverse rows
    return [item for row in rotated for item in row]  # flatten




def flip_vertical_1d(arr, cols=3):
    rows = [arr[i:i+cols] for i in range(0, len(arr), cols)]
    flipped = rows[::-1]  # reverse rows
    return [item for row in flipped for item in row]  # flatten

def to_2d(arr, size=3):
    return [arr[i:i+size] for i in range(0, len(arr), size)]

def to_1d(grid):
    return [item for row in grid for item in row]
def flip_y_axis(arr):
    grid = to_2d(arr)
    for i in range(len(grid)):
        grid[i] = grid[i][::-1]
    return to_1d(grid)
def flip_x_axis(arr):
    grid = to_2d(arr)
    grid = grid[::-1]
    return to_1d(grid)
def rotate_left(arr):
    grid = to_2d(arr)
    rotated = list(zip(*grid))[::-1]  # transpose + flip vertically
    rotated = [list(row) for row in rotated]
    return to_1d(rotated)


blueh = flip_y_axis(blueh)#blueh=greenh
greenh=rotate_90_right(greenh)#greeh=blueh
greenh=rotate_90_right(greenh)#greeh=blueh,greenh[7]=greenh[7]

redh=rotate_90_right(redh)

redh=rotate_90_right(redh)
redh[1], redh[3] = redh[3], redh[1]
redh[5], redh[7] = redh[7], redh[5]
redh[2], redh[6] = redh[6], redh[2]
yellowh = flip_vertical_1d(yellowh)
class Cube:
    """Magic Cube Representation"""
    # define some attribues
    default_plastic_color = 'black'
    default_face_colors = ["w", "#ffcf00",
                           "#00008f", "#009f0f",
                           "#ff6f00", "#cf0000",
                           "gray", "none"]
    base_face = np.array([[1, 1, 1],
                          [1, -1, 1],
                          [-1, -1, 1],
                          [-1, 1, 1],
                          [1, 1, 1]], dtype=float)
    stickerwidth = 0.9
    stickermargin = 0.5 * (1. - stickerwidth)
    stickerthickness = 0.001
    (d1, d2, d3) = (1 - stickermargin,
                    1 - 2 * stickermargin,
                    1 + stickerthickness)
    base_sticker = np.array([[d1, d2, d3], [d2, d1, d3],
                             [-d2, d1, d3], [-d1, d2, d3],
                             [-d1, -d2, d3], [-d2, -d1, d3],
                             [d2, -d1, d3], [d1, -d2, d3],
                             [d1, d2, d3]], dtype=float)

    base_face_centroid = np.array([[0, 0, 1]])
    base_sticker_centroid = np.array([[0, 0, 1 + stickerthickness]])

    # Define rotation angles and axes for the six sides of the cube
    x, y, z = np.eye(3)
    rots = [Quaternion.from_v_theta(np.eye(3)[0], theta)
    for theta in (np.pi / 2, -np.pi / 2)]
    rots += [Quaternion.from_v_theta(np.eye(3)[1], theta)
    for theta in (np.pi / 2, -np.pi / 2, np.pi, 2 * np.pi)]

    # define face movements
    facesdict = dict(F=z, B=-z,
                     R=x, L=-x,
                     U=y, D=-y)

    def __init__(self, N=3, plastic_color=None, face_colors=None):
        self.N = N
        if plastic_color is None:
            self.plastic_color = self.default_plastic_color
        else:
            self.plastic_color = plastic_color

        if face_colors is None:
            self.face_colors = self.default_face_colors
                # Swap orange (index 4) and red (index 5)
            self.face_colors = self.face_colors.copy()
            self.face_colors[4], self.face_colors[5] = self.face_colors[5], self.face_colors[4]

        else:
            self.face_colors = face_colors

        self._move_list = []
        self._initialize_arrays()

    def _initialize_arrays(self):
        # initialize centroids, faces, and stickers.  We start with a
        # base for each one, and then translate & rotate them into position.

        # Define N^2 translations for each face of the cube
        cubie_width = 2. / self.N
        translations = np.array([[[-1 + (i + 0.5) * cubie_width,
                                   -1 + (j + 0.5) * cubie_width, 0]]
                                 for i in range(self.N)
                                 for j in range(self.N)])

        # Create arrays for centroids, faces, stickers, and colors
        face_centroids = []
        faces = []
        sticker_centroids = []
        stickers = []
        colors = []

        factor = np.array([1. / self.N, 1. / self.N, 1])

        for i in range(6):
            M = self.rots[i].as_rotation_matrix()
            faces_t = np.dot(factor * self.base_face
                             + translations, M.T)
            stickers_t = np.dot(factor * self.base_sticker
                                + translations, M.T)
            face_centroids_t = np.dot(self.base_face_centroid
                                      + translations, M.T)
            sticker_centroids_t = np.dot(self.base_sticker_centroid
                                         + translations, M.T)
            colors_i = i + np.zeros(face_centroids_t.shape[0], dtype=int)

            # append face ID to the face centroids for lex-sorting
            face_centroids_t = np.hstack([face_centroids_t.reshape(-1, 3),
                                          colors_i[:, None]])
            sticker_centroids_t = sticker_centroids_t.reshape((-1, 3))

            faces.append(faces_t)
            face_centroids.append(face_centroids_t)
            stickers.append(stickers_t)
            sticker_centroids.append(sticker_centroids_t)
            colors.append(colors_i)

        self._face_centroids = np.vstack(face_centroids)
        self._faces = np.vstack(faces)
        self._sticker_centroids = np.vstack(sticker_centroids)
        self._stickers = np.vstack(stickers)
        self._colors = np.concatenate(colors)

        self._sort_faces()

    def _sort_faces(self):
        # use lexsort on the centroids to put faces in a standard order.
        ind = np.lexsort(self._face_centroids.T)
        self._face_centroids = self._face_centroids[ind]
        self._sticker_centroids = self._sticker_centroids[ind]
        self._stickers = self._stickers[ind]
        self._colors = self._colors[ind]
        self._faces = self._faces[ind]

    def rotate_face(self, f, n=1, layer=0):
        """Rotate Face"""
        if layer < 0 or layer >= self.N:
            raise ValueError('layer should be between 0 and N-1')

        try:
            f_last, n_last, layer_last = self._move_list[-1]
        except:
            f_last, n_last, layer_last = None, None, None

        if (f == f_last) and (layer == layer_last):
            ntot = (n_last + n) % 4
            if abs(ntot - 4) < abs(ntot):
                ntot = ntot - 4
            if np.allclose(ntot, 0):
                self._move_list = self._move_list[:-1]
            else:
                self._move_list[-1] = (f, ntot, layer)
        else:
            self._move_list.append((f, n, layer))
        
        v = self.facesdict[f]
        r = Quaternion.from_v_theta(v, n * np.pi / 2)
        M = r.as_rotation_matrix()

        proj = np.dot(self._face_centroids[:, :3], v)
        cubie_width = 2. / self.N
        flag = ((proj > 0.9 - (layer + 1) * cubie_width) &
                (proj < 1.1 - layer * cubie_width))

        for x in [self._stickers, self._sticker_centroids,
                  self._faces]:
            x[flag] = np.dot(x[flag], M.T)
        self._face_centroids[flag, :3] = np.dot(self._face_centroids[flag, :3],
                                                M.T)

    def draw_interactive(self):
        fig = plt.figure(figsize=(5, 5))
        fig.add_axes(InteractiveCube(self))
        return fig


class InteractiveCube(plt.Axes):
    def _play_moves(self, event):
        faces = [white, blue, red, yellow, green, orange]

        # Create color map based on center stickers
        color_map = {
            white[4]: 'U',   # white center
            blue[4]: 'R',    # blue center
            red[4]: 'F',     # red center
            yellow[4]: 'D',  # yellow center
            green[4]: 'L',   # green center
            orange[4]: 'B'   # orange center
        }

        # Convert to 54-letter cube string
        cube_str = ''.join(color_map[color] for face in faces for color in face)

        # Solve
        solution = tw.solve(cube_str)

        # Output
        print("Cube string:", cube_str)
        print("Solution:", solution)
        solution = solution[:-5]
        pr = str(solution)
        moves = parse_moves(pr)
        for face, count in moves:
            self.rotate_face(face, count)

    def __init__(self, cube=None,
                 interactive=True,
                 view=(0, 0, 10),
                 fig=None, rect=[0, 0.16, 1, 0.84],
                 **kwargs):
        if cube is None:
            self.cube = Cube(3)
        elif isinstance(cube, Cube):
            self.cube = cube
        else:
            self.cube = Cube(cube)

        self._view = view
        self._start_rot = Quaternion.from_v_theta((1, -1, 0),
                                                  -np.pi / 6)

        if fig is None:
            fig = plt.gcf()

        # disable default key press events
        callbacks = fig.canvas.callbacks.callbacks
        del callbacks['key_press_event']

        # add some defaults, and draw axes
        kwargs.update(dict(aspect=kwargs.get('aspect', 'equal'),
                           xlim=kwargs.get('xlim', (-2.0, 2.0)),
                           ylim=kwargs.get('ylim', (-2.0, 2.0)),
                           frameon=kwargs.get('frameon', False),
                           xticks=kwargs.get('xticks', []),
                           yticks=kwargs.get('yticks', [])))
        super(InteractiveCube, self).__init__(fig, rect, **kwargs)
        self.xaxis.set_major_formatter(plt.NullFormatter())
        self.yaxis.set_major_formatter(plt.NullFormatter())

        self._start_xlim = kwargs['xlim']
        self._start_ylim = kwargs['ylim']

        # Define movement for up/down arrows or up/down mouse movement
        self._ax_UD = (1, 0, 0)
        self._step_UD = 0.01

        # Define movement for left/right arrows or left/right mouse movement
        self._ax_LR = (0, -1, 0)
        self._step_LR = 0.01

        self._ax_LR_alt = (0, 0, 1)

        # Internal state variable
        self._active = False  # true when mouse is over axes
        self._button1 = False  # true when button 1 is pressed
        self._button2 = False  # true when button 2 is pressed
        self._event_xy = None  # store xy position of mouse event
        self._shift = False  # shift key pressed
        self._digit_flags = np.zeros(10, dtype=bool)  # digits 0-9 pressed

        self._current_rot = self._start_rot  #current rotation state
        self._face_polys = None
        self._sticker_polys = None

        self._draw_cube()

        # connect some GUI events
        self.figure.canvas.mpl_connect('button_press_event',
                                       self._mouse_press)
        self.figure.canvas.mpl_connect('button_release_event',
                                       self._mouse_release)
        self.figure.canvas.mpl_connect('motion_notify_event',
                                       self._mouse_motion)
        self.figure.canvas.mpl_connect('key_press_event',
                                       self._key_press)
        self.figure.canvas.mpl_connect('key_release_event',
                                       self._key_release)

        self._initialize_widgets()

        # write some instructions
        self.figure.text(0.05, 0.05,
                         "Mouse/arrow keys adjust view\n"
                         "U/D/L/R/B/F keys turn faces\n"
                         "(hold shift for counter-clockwise)",
                         size=10)

    def _initialize_widgets(self):
        self._ax_reset = self.figure.add_axes([0.75, 0.05, 0.2, 0.075])
        self._btn_reset = widgets.Button(self._ax_reset, 'Reset View')
        self._btn_reset.on_clicked(self._reset_view)

        self._ax_solve = self.figure.add_axes([0.55, 0.05, 0.2, 0.075])
        self._btn_solve = widgets.Button(self._ax_solve, 'Solve Cube')
        self._btn_solve.on_clicked(self._solve_cube)
        self._ax_play = self.figure.add_axes([0.75, 0.125, 0.2, 0.075])
        self._btn_play = widgets.Button(self._ax_play, 'Play Moves')
        self._btn_play.on_clicked(self._play_moves)



    def _project(self, pts):
        return project_points(pts, self._current_rot, self._view, [0, 1, 0])

    def _draw_cube(self):
        global abc
        global wooo
        stickers = self._project(self.cube._stickers)[:, :, :2]
        faces = self._project(self.cube._faces)[:, :, :2]
        face_centroids = self._project(self.cube._face_centroids[:, :3])
        sticker_centroids = self._project(self.cube._sticker_centroids[:, :3])

        plastic_color = self.cube.plastic_color
        colors = np.asarray(self.cube.face_colors)[self.cube._colors]
        face_zorders = -face_centroids[:, 2]
        sticker_zorders = -sticker_centroids[:, 2]

        if self._face_polys is None:
            # initial call: create polygon objects and add to axes
            self._face_polys = []
            self._sticker_polys = []

            for i in range(len(colors)):
                fp = plt.Polygon(faces[i], facecolor=plastic_color,
                                 zorder=face_zorders[i])
                sp = plt.Polygon(stickers[i], facecolor="gray",
                                            
                                 zorder=sticker_zorders[i])
                
                self._face_polys.append(fp)
                self._sticker_polys.append(sp)
                self.add_patch(fp)
                self.add_patch(sp)


        if (self._face_polys is not None) or (abc==1):
            # subsequent call: update the polygon objects
            for i in range(len(colors)):
                self._face_polys[i].set_xy(faces[i])
                self._face_polys[i].set_zorder(face_zorders[i])
                self._face_polys[i].set_facecolor(plastic_color)

                self._sticker_polys[i].set_xy(stickers[i])
                self._sticker_polys[i].set_zorder(sticker_zorders[i])
                self._sticker_polys[i].set_facecolor("gray")
                
                self._sticker_polys[0].set_facecolor("w")
                self._sticker_polys[4].set_facecolor("w")#up
                self._sticker_polys[5].set_facecolor("w")
                self._sticker_polys[13].set_facecolor("#ffcf00")#down
                self._sticker_polys[22].set_facecolor("#00008f")#left
                self._sticker_polys[31].set_facecolor("#009f0f")#right
                self._sticker_polys[49].set_facecolor("#ff6f00")#front
                self._sticker_polys[38].set_facecolor("#cf0000")#back
                for j in range(len(whiteh)):
                    self._sticker_polys[j].set_facecolor(whiteh[j])
                for j in range(len(yellowh)):
                                    self._sticker_polys[j+9].set_facecolor(yellowh[j])
                for j in range(len(blueh)):
                                    self._sticker_polys[j+18].set_facecolor(blueh[j])
                for j in range(len(greenh)):
                                    self._sticker_polys[j+27].set_facecolor(greenh[j])
                for j in range(len(orangeh)):
                                    self._sticker_polys[j+36].set_facecolor(orangeh[j])
                                    print (self._sticker_polys[j+36])
                for j in range(len(redh)):
                                    self._sticker_polys[j+45].set_facecolor(redh[j])

                # self._sticker_polys[15].set_facecolor("#ffcf00")#down
                # self._sticker_polys[22].set_facecolor("#00008f")#left
                # self._sticker_polys[31].set_facecolor("#009f0f")#right
                # self._sticker_polys[47].set_facecolor("#ff6f00")#front
                # self._sticker_polys[38].set_facecolor("#cf0000")#back
                print(wooo)
                wooo+=1
                abc = 0

        self.figure.canvas.draw()

    def rotate(self, rot):
        self._current_rot = self._current_rot * rot

    def rotate_face(self, face, turns=1, layer=0, steps=5):
        if not np.allclose(turns, 0):
            for i in range(steps):
                plt.pause(0.02)
                self.cube.rotate_face(face, turns * 1. / steps,
                                      layer=layer)
                self._draw_cube()

    def _reset_view(self, *args):
        self.set_xlim(self._start_xlim)
        self.set_ylim(self._start_ylim)
        self._current_rot = self._start_rot
        self._draw_cube()

    def _solve_cube(self, *args):
        move_list = self.cube._move_list[:]
        for (face, n, layer) in move_list[::-1]:
            self.rotate_face(face, -n, layer, steps=3)
        self.cube._move_list = []

    def _key_press(self, event):
        """Handler for key press events"""
        if event.key == 'shift':
            self._shift = True
        elif event.key.isdigit():
            self._digit_flags[int(event.key)] = 1
        elif event.key == 'right':
            if self._shift:
                ax_LR = self._ax_LR_alt
            else:
                ax_LR = self._ax_LR
            self.rotate(Quaternion.from_v_theta(ax_LR,
                                                5 * self._step_LR))
        elif event.key == 'left':
            if self._shift:
                ax_LR = self._ax_LR_alt
            else:
                ax_LR = self._ax_LR
            self.rotate(Quaternion.from_v_theta(ax_LR,
                                                -5 * self._step_LR))
        elif event.key == 'up':
            self.rotate(Quaternion.from_v_theta(self._ax_UD,
                                                5 * self._step_UD))
        elif event.key == 'down':
            self.rotate(Quaternion.from_v_theta(self._ax_UD,
                                                -5 * self._step_UD))
        elif event.key.upper() in 'LRUDBF':
            if self._shift:
                direction = -1
            else:
                direction = 1

            if np.any(self._digit_flags[:N]):
                for d in np.arange(N)[self._digit_flags[:N]]:
                    self.rotate_face(event.key.upper(), direction, layer=d)
            else:
                self.rotate_face(event.key.upper(), direction)
                
        self._draw_cube()

    def _key_release(self, event):
        """Handler for key release event"""
        if event.key == 'shift':
            self._shift = False
        elif event.key.isdigit():
            self._digit_flags[int(event.key)] = 0

    def _mouse_press(self, event):
        """Handler for mouse button press"""
        self._event_xy = (event.x, event.y)
        if event.button == 1:
            self._button1 = True
        elif event.button == 3:
            self._button2 = True

    def _mouse_release(self, event):
        """Handler for mouse button release"""
        self._event_xy = None
        if event.button == 1:
            self._button1 = False
        elif event.button == 3:
            self._button2 = False

    def _mouse_motion(self, event):
        """Handler for mouse motion"""
        if self._button1 or self._button2:
            dx = event.x - self._event_xy[0]
            dy = event.y - self._event_xy[1]
            self._event_xy = (event.x, event.y)

            if self._button1:
                if self._shift:
                    ax_LR = self._ax_LR_alt
                else:
                    ax_LR = self._ax_LR
                rot1 = Quaternion.from_v_theta(self._ax_UD,
                                               self._step_UD * dy)
                rot2 = Quaternion.from_v_theta(ax_LR,
                                               self._step_LR * dx)
                self.rotate(rot1 * rot2)

                self._draw_cube()

            if self._button2:
                factor = 1 - 0.003 * (dx + dy)
                xlim = self.get_xlim()
                ylim = self.get_ylim()
                self.set_xlim(factor * xlim[0], factor * xlim[1])
                self.set_ylim(factor * ylim[0], factor * ylim[1])

                self.figure.canvas.draw()

if __name__ == '__main__':
    import sys
    try:
        N = int(sys.argv[1])
    except:
        N = 3

    c = Cube(N)

    # do a 3-corner swap
    #c.rotate_face('R')
    #c.rotate_face('D')
    #c.rotate_face('R', -1)
    #c.rotate_face('U', -1)
    #c.rotate_face('R')
    #c.rotate_face('D', -1)
    #c.rotate_face('R', -1)
    #c.rotate_face('U')

    c.draw_interactive()

    plt.show()



