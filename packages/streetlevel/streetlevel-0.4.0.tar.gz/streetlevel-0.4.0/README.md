# streetlevel
**streetlevel** is a module for downloading panoramas and metadata from street-level imagery services including Google Street View and Apple Look Around.

Since it relies on calls to internal APIs, it may break unexpectedly.

## Installation
```sh
pip install streetlevel
```

## Example
Downloading the closest Street View panorama to a specific location:

```python
from streetlevel import streetview

pano = streetview.find_panorama(46.8839586, 12.169002)
streetview.download_panorama(pano, f"{pano.id}.jpg")
```

## Documentation
Documentation is available at [streetlevel.readthedocs.io](https://streetlevel.readthedocs.io/).

## Functionality overview
✔ implemented / available; 🟡 partially implemented / available; ❌ not implemented; ⚫ not available / not applicable

<table>
  <thead>
    <th></th>
    <th align="center">Street View</th>
    <th align="center">Look Around</th>
    <th align="center">Streetside</th>
    <th align="center">Mapy.cz Panorama</th>
  </thead>
  <thead>
    <td colspan="5" style="padding-top:20px"><b>Finding panoramas</b><br>
      How panoramas can be retrieved through the API.
    </td>
  </thead>
  <tr>
    <td align="right">Find panoramas around a point</td>
    <td align="center">✔<br>
      (returns closest only)
    </td>
    <td align="center">⚫</td>
    <td align="center">✔</td>
    <td align="center">✔<br>
      (returns closest only)
    </td>
  </tr>
  <tr>
    <td align="right">Find panoramas by slippy map tile or bounding box</td>
    <td align="center">✔<br>
      (tile, z=17)
    </td>
    <td align="center">✔<br>
      (tile, z=17)
    </td>
    <td align="center">✔<br>
      (bounding box)
    </td>
    <td align="center">⚫</td>
  </tr>
  <tr>
    <td align="right">Get specific panorama by ID</td>
    <td align="center">✔</td>
    <td align="center">⚫</td>
    <td align="center">✔</td>
    <td align="center">⚫</td>
  </tr>
  <thead>
    <td colspan="5" style="padding-top:20px"><b>Imagery</b><br>
      The type of imagery returned by the service.
    </td>
  </thead>
  <tr>
    <td align="right">Download panoramas</td>
    <td align="center">✔</td>
    <td align="center">✔<br>(unstitched)</td>
    <td align="center">✔</td>
    <td align="center">✔</td>
  </tr>
  <tr>
    <td align="right">Download depth information</td>
    <td align="center">✔<br>(simplified)</td>
    <td align="center">❌</td>
    <td align="center">⚫</td>
    <td align="center">⚫<br>(?)</td>
  </tr>
  <tr>
    <td align="right">Image projection</td>
    <td align="center">Equirectangular</td>
    <td align="center">???</td>
    <td align="center">Cubemap</td>
    <td align="center">Equirectangular</td>
  </tr>
  <tr>
    <td align="right">Image format</td>
    <td align="center">JPEG</td>
    <td align="center">HEIC</td>
    <td align="center">JPEG</td>
    <td align="center">JPEG</td>
  </tr>
  <thead>
    <td colspan="5" style="padding-top:20px"><b>Available metadata</b><br>
      Metadata returned by the API of the service alongside ID and location.
    </td>
  </thead>
  <tr>
    <td align="right">Capture date</td>
    <td align="center">✔<br>
      (month and year only for official coverage; full date for inofficial coverage)
    </td>
    <td align="center">✔</td>
    <td align="center">✔</td>
    <td align="center">✔</td>
  </tr>
  <tr>
    <td align="right">Heading, pitch, roll</td>
    <td align="center">✔</td>
    <td align="center">🟡<br>(only heading is implemented; inaccurate in some locations)</td>
    <td align="center">✔</td>
    <td align="center">✔<br></td>
  </tr>
  <tr>
    <td align="right">Elevation</td>
    <td align="center">⚫</td>
    <td align="center">❌</td>
    <td align="center">✔</td>
    <td align="center">✔</td>
  </tr>
  <tr>
    <td align="right">Nearby / linked panoramas</td>
    <td align="center">✔</td>
    <td align="center">⚫</td>
    <td align="center">✔<br>
      (previous and next image in sequence)
    </td>
    <td align="center">✔</td>
  </tr>
  <tr>
    <td align="right">Historical panoramas</td>
    <td align="center">✔</td>
    <td align="center">⚫</td>
    <td align="center">⚫</td>
    <td align="center">✔</td>
  </tr>
  <tr>
    <td align="right">Address</td>
    <td align="center">✔</td>
    <td align="center">⚫</td>
    <td align="center">⚫</td>
    <td align="center">⚫</td>
  </tr>
  <tr>
    <td align="right">Creator</td>
    <td align="center">✔</td>
    <td align="center">⚫</td>
    <td align="center">⚫</td>
    <td align="center">✔</td>
  </tr>
</table>
