# yt-wrapper <!-- omit in toc -->
**A simple wrapper around the Youtube Data API.**
***

**Table of contents**
- [Introduction](#introduction)
- [Tutorial/Quickstart](#tutorialquickstart)
- [Guides](#guides)
- [API Reference](#api-reference)
  - [`Client`](#client)
  - [Methods](#methods)
    - [`Playlist`](#playlist)
    - [`PlaylistItem`](#playlistitem)
    - [`Thumbnail`](#thumbnail)
    - [`Comment`](#comment)
    - [`CommentThread`](#commentthread)
    - [`I18n`](#i18n)
    - [`VideoCategory`](#videocategory)
    - [`VideoAbuseReportReason`](#videoabusereportreason)
    - [`Video`](#video)
    - [`Channel`](#channel)
    - [`ChannelSection`](#channelsection)
    - [`Search`](#search)
    - [`Subscription`](#subscription)
  - [Resources](#resources)
    - [`PlaylistResource`](#playlistresource)
    - [`PlaylistItemResource`](#playlistitemresource)
    - [`ThumbnailResource`](#thumbnailresource)
    - [`CommentResource`](#commentresource)
    - [`CommentThreadResource`](#commentthreadresource)
    - [`I18nLanguageResource`](#i18nlanguageresource)
    - [`I18nRegionResource`](#i18nregionresource)
    - [`VideoCategoryResource`](#videocategoryresource)
    - [`VideoAbuseReportReasonResource`](#videoabusereportreasonresource)
    - [`VideoResource`](#videoresource)
    - [`ChannelResource`](#channelresource)
    - [`ChannelSectionResource`](#channelsectionresource)
    - [`SearchResult`](#searchresult)
    - [`SubscriptionResource`](#subscriptionresource)
    - [`PlaylistListResponse`](#playlistlistresponse)
    - [`PlaylistItemListResponse`](#playlistitemlistresponse)
    - [`ThumbnailListResponse`](#thumbnaillistresponse)
    - [`CommentListResponse`](#commentlistresponse)
    - [`CommentThreadListResponse`](#commentthreadlistresponse)
    - [`I18nLanguageListResponse`](#i18nlanguagelistresponse)
    - [`I18nRegionListResponse`](#i18nregionlistresponse)
    - [`VideoCategoryListResponse`](#videocategorylistresponse)
    - [`VideoAbuseReportReasonListResponse`](#videoabusereportreasonlistresponse)
    - [`VideoListResponse`](#videolistresponse)
    - [`ChannelListResponse`](#channellistresponse)
    - [`ChannelSectionListResponse`](#channelsectionlistresponse)
    - [`SearchListResponse`](#searchlistresponse)
    - [`SubscriptionListResponse`](#subscriptionlistresponse)

## Introduction
The goal of this project is to create an (almost) complete, comprehensive Python wrapper for the Youtube Data API. 

**WARNING:** *This project is still unfinished. Breaking changes can be made at any time. Usse at your own risk.*

**NOTE:** This project is my first ever attempt at creating a semi-decent Python package.
## Tutorial/Quickstart 

This section will demonstrate a simple program written using this package. We will be retrieving a video's title with it's ID.

For the full documentation for this package, see the [API Reference](#api-reference).  

1. **Package installation** 
   
    To use this package, you must have `Python 3.10` or higher.

    Install using `pip`:
    ```
    pip install yt-wrapper
    ```
    It is recommended that you use a virtual environment when installing this package.

2. **Authorization**

    *TODO: write the authorizaton process.*

3. **Using the API**
    
    - Setting up the client  

        ```python
        from ytwrapper.client import Client
        youtube = Client.from_client_secrets(path_to_client_secrets_file, scopes=['https://www.googleapis.com/auth/youtube.readonly'])
        ```
    - Getting the video

        ```python
        video = youtube.video.list(
            part='snippet',        # the `snippet` part, which contains the video titles
            id='dQw4w9WgXcQ'       # the Video id of the video we're retrieving
        )

        print(video.snippet.title) # Output: 'Rick Astley - Never Gonna Give You Up (Official Music Video)'
        ```

## Guides

## API Reference

### `Client`
The `Client` class represents a Youtube client, containing the entire API of this project.

**Methods:**
- `from_client_secrets` 
    
    Creates a new `Client` object from an OAuth2 [Installed App](https://developers.google.com/youtube/v3/guides/auth/installed-apps) client secrets file. Will prompt the user to go to a link and give access, where the user will have to copy a code given at the end to the terminal.
    - `client_secrets_file: str`
        
        The path to the client secrets JSON file. This file should contain the client secrets of an [Installed App project.](https://developers.google.com/youtube/v3/guides/auth/installed-apps)
    - `scopes: list[str]`

        [The scope of the program](https://developers.google.com/youtube/v3/guides/auth/installed-apps#identify-access-scopes), specifying the permissions the user must give. Each method in the API has it's own scopes that it needs for it to be used.
    - `token_store: str = "token.pickle"`

        The path to the file used to store the OAuth2 access and refresh token.

**Attributes:**
- `playlist`: The interface for [Playlist](#playlist).
- `playlist_item`: The interface for [PlaylistItem](#playlistitem).
- `thumbnail`: The interface for [Thumbnail](#thumbnail).
- `comment`: The interface for [Comment](#comment).
- `comment_thread`: The interface for [CommentThread](#commentthread).
- `i18n`: The interface for [I18n](#i18n).
- `video_category`: The interface for [VideoCategory](#videocategry).
- `video_abuse_report_reason`: The interface for [VideoAbuseReportReason](#videoabusereportreason).
- `video`: The interface for [Video](#video).
- `channel`: The interface for [Channel](#channel).
- `channel_section`: The interface for [ChannelSection](#channelsection).
- `search`: The interface for [Search](#search).
- `subscription`: The interface for [Subscription](#subscription).

***
### Methods
<!-- TODO: Add in return types for each of these. -->
This section describes the methods available in the API. These methods are accessible via the [`Client`](#client) object.

<!--m-start Playlist -->
#### `Playlist`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Returns a collection of playlists.  
    **Required** parameters:
    - `part: PlaylistPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id: list[str]|str`

        The playlist ID/list of playlist IDs that will be returned.
    - `channel_id: str`

        Specifies a channel ID whose playlists will be returned.
    - `mine: bool`

        Specifies that the API should retrieve the playlists of the authorised user.

    **Optional** parameters:
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistListResponse`](#playlistlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Creates a playlist.  
    **Required** parameters:
    - `body: [PlaylistResource](#playlistresource)`

        The [`PlaylistResource`](#playlistresource) which specifies the details of this playlist.  
        **Values you are able to set**:
        - `snippet.title` (Required)
        - `snippet.description`
        - `snippet.privacy_status`
    - `part: PlaylistPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistResource`](#playlistresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a playlist.  
    **Required** parameters:
    - `body: PlaylistResource`

        The [`PlaylistResource`](#playlistresource) which specifies the details of this playlist.  
        **Values you are able to set**:
        - `id` (Required)
        - Otherwise, same as the above `insert` method.`
    - `part: PlaylistPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistResource`](#playlistresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a playlist.  
    **Required** parameters:
    - `playlist_id: str`

        The ID of the playlist that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/delete)
</details>

<!--m-end Playlist -->
<!--m-start PlaylistItem -->
#### `PlaylistItem`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Returns a collection of playlist items that match the API request parameters.  
    **Required** parameters:
    - `part: PlaylistItemPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id: list[str]|str`

        The ID/list of IDs of the playlist items that should be returned.
    - `playlist_id: str`

        The ID of the playlist whose videos will be retrieved.

    **Optional** parameters:
    - `video_id: str`

        Specifies that the request should return only the playlist items that contain the specified video.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistItemListResponse`](#playlistitemlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/playliststems/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Modifies a playlist item.  
    **Required** parameters:
    - `body: PlaylistItemResource`

        The [`PlaylistItemResource`](#playlistitemresource) which specifies the details of the playlist item.  
        **Values you are able to set**:
        - `snippet.playlist_id` (Required)
        - `snippet.resource_id` (Required)
        - `snippet.position`
        - `content_details.note`
        - `content_details.start_at`
        - `content_details.end_at`
    - `part: PlaylistItemPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistItemResource`](#playlistitemresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlistItems/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Inserts a video into a playlist.  
    **Required** parameters:
    - `body: PlaylistItemResource`

        The [`PlaylistItemResource`](#playlistitemresource) which specifies the details of the playlist item.  
        **Values you are able to set**:
        - `id` (Required)
        - Otherwise, same as the above `insert` method.`
    - `part: PlaylistItemPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistItemResource`](#playlistitemresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlistItems/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a playlist item.  
    **Required** parameters:
    - `playlist_item_id: str`

        The ID of the playlist item that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/playlistItems/delete)
</details>

<!--m-end PlaylistItem -->
<!--m-start Thumbnail -->
#### `Thumbnail`
**Methods:**
- <details><summary><code>set</code></summary>
    <br>

    Uploads a custom video thumbnail to YouTube and sets it for a video.  
    **Required** parameters:
    - `thumbnail_file: str`

        The path to the file of the thumbnail.
    - `video_id: str`

        The ID of the video for the thumbnail.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ThumbnailListResponse`](#thumbnaillistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/thumbnails/set)
</details>

<!--m-end Thumbnail -->
<!--m-start Comment -->
#### `Comment`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of comments.  
    **Required** parameters:
    - `part: CommentPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id`

        The id of the comment that should be retrived.
    - `parent_id`

        The ID of the top-level comment whose replies should be retrieved.

    **Optional** parameters:
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `text_format: Literal['html', 'plain_text']`

        The format of the returned comment.

    **Returns:** [`CommentListResponse`](#commentlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/comments/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Create a reply to a top-level comment. To create a top-level comment, use CommentThread.insert instead.  
    **Required** parameters:
    - `body: CommentResource`

        The [`CommentResource`](#commentresource) which specifies the details of the reply.  
        **Values you are able to set**:
        - `snippet.text_original`
        - `snippet.parent_id`
    - `part: CommentPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Returns:** [`CommentResource`](#commentresource)

    [Reference](https://developers.google.com/youtube/v3/docs/comments/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Modifies a comment.  
    **Required** parameters:
    - `body: CommentResource`

        The [`CommentResource`](#commentresource) which specifies the details of the comment.  
        **Values you are able to set**:
        - `id`(Required)
        - `snippet.text_original`
    - `part: CommentPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Returns:** [`CommentResource`](#commentresource)

    [Reference](https://developers.google.com/youtube/v3/docs/comments/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a comment.  
    **Required** parameters:
    - `comment_id: str`

        The ID of the comment that should be deleted.

    [Reference](https://developers.google.com/youtube/v3/docs/comments/delete)
</details>

<!--m-end Comment -->
<!--m-start CommentThread -->
#### `CommentThread`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of comment threads.  
    **Required** parameters:
    - `part: CommentThreadPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id: str`

        The ID of the comment.
    - `channel_id: str`

        Specifies the API to retrieve all comment threads which contain comments from this channel.
    - `video_id: str`

        Specifies the ID of the video whose comments should be retrieved.
    - `all_threads_related_to_channel_id: str`

        Specifies the API to return all comment threads associated with the specified channel.

    **Optional** parameters:
    - `moderation_status: Literal['held_for_review', 'likely_spam', 'published']`

        Specifies that all returned comments are of the given moderation state.
    - `order: Literal['time', 'relevance']`

        Specifies the order the returned comment threads should be in.
    - `text_format: Literal['html', 'plain_text']`

        The format of the returned comment.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`CommentThreadListResponse`](#commentthreadlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/commentThreads/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Create a new top-level comment.  
    **Required** parameters:
    - `body: CommentThreadResource`

        The [`CommentThreadResource`](#commentthreadresource) which specifies the details of the comment.  
        **Values you are able to set**:
        - `snippet.channel_id`
        - `snippet.video_id`
        - `snippet.top_level_comment.snippet.text_original`
    - `part: CommentThreadPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Returns:** [`CommentThreadResource`](#commentthreadresource)

    [Reference](https://developers.google.com/youtube/v3/docs/commentThreads/insert)
</details>

<!--m-end CommentThread -->
<!--m-start I18n -->
#### `I18n`
**Methods:**
- <details><summary><code>list_languages</code></summary>
    <br>

    Returns a list of languages that YouTube supports.  
    **Returns:** [`I18nLanguageListResponse`](#i18nlanguagelistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/i18nLanguages/list/)
</details>

- <details><summary><code>list_regions</code></summary>
    <br>

    Returns a list of content regions that YouTube supports.  
    **Returns:** [`I18nLanguageRegionResponse`](#i18nlanguageregionresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/i18nRegions/list/)
</details>

<!--m-end I18n -->
<!--m-start VideoCategory -->
#### `VideoCategory`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Returns a list of categories that can be associated with YouTube videos.  
    **Optional** parameters:
    - `id: str|list[str]`

        The ID of the video category to be retrieved.
    - `region_code: str`

        Specifies the API to retrive all video categories in the specified region code.

    **Returns:** [`VideoCategoryListResponse`](#videocategorylistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/videoCategories/list)
</details>

<!--m-end VideoCategory -->
<!--m-start VideoAbuseReportReason -->
#### `VideoAbuseReportReason`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of reasons that can be used to report abusive videos.  
    **Returns:** [`VideoAbuseReportReasonListResponse`](#videoabusereportreasonlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list)
</details>

<!--m-end VideoAbuseReportReason -->
<!--m-start Video -->
#### `Video`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieves a list of videos.  
    **Required** parameters:
    - `part: VideoPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `chart: Literal['most_popular']`

        Identifies the chart that you want to retrieve.
    - `id: list[str]|str`

        Specifies the video(s) that should be retrieved.
    - `my_rating: Literal["like", "dislike"]`

        Specifies that the API should only retrieve videos that the user has disliked/like.

    **Optional** parameters:
    - `region_code: str`

        Specifies the API to select a video chart in the specified region code.
        Used in conjunction with the `chart` parameter.
    - `video_category_id: str`

        Specifies the video category for which the chart should be retrieved.
        Used in conjunction with the `chart` parameter.
    - `max_height: int`

        Specifies the maximum height of the embedded player returned in the `player.embed_html` property
    - `max_width: int`

        Specifies the maximum width of the embedded player returned in the `player.embed_html` property
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`VideoListResponse`](#videolistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/videos/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Upload a video to youtube.  
    **Required** parameters:
    - `body: VideoResource`

        The [`VideoResource`](#videoresource) which specifies the details of the comment.  
        **Values you are able to set**:
        - `snippet.title`
        - `snippet.description`
        - `snippet.tags`
        - `snippet.category_id`
        - `snippet.default_language`
        - `status.embeddable`
        - `status.license`
        - `status.public_stats_viewable`
        - `status.publish_at`
        - `status.self_declared_made_for_kids`
        - `recording_details.recording_date`
    - `part: VideoPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `media_body: str`

        The path to the file of the uploaded video.

    **Optional** parameters:
    - `notify_subscribers: bool`

        Indicates whether YouTube should notify subscribers to the video's channel about the video.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`VideoResource`](#videoresource)

    [Reference](https://developers.google.com/youtube/v3/docs/videos/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a video's metadata.  
    **Required** parameters:
    - `body: VideoResource`

        The [`VideoResource`](#videoresource) which specifies the details of the video.  
        **Values you are able to set**:
        - `id` (Required)
        - `snippet.title (Required IF updating the `snippet` attribute.)`
        - `snippet.description`
        - `snippet.tags`
        - `snippet.category_id`
        - `snippet.default_language`
        - `status.embeddable`
        - `status.license`
        - `status.public_stats_viewable`
        - `status.publish_at`
        - `status.self_declared_made_for_kids`
        - `recording_details.recording_date`
    - `part: VideoPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`VideoResource`](#videoresource)

    [Reference](https://developers.google.com/youtube/v3/docs/videos/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a video.  
    **Required** parameters:
    - `video_id: str`

        The ID of the Video that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/videos/delete)
</details>

- <details><summary><code>rate</code></summary>
    <br>

    Rate a video.  
    **Required** parameters:
    - `video_id: str`

        The ID of the Video to rate.
    - `rating: Literal['dislike', 'like', 'none']`

        The rating to give to the video.

    [Reference](https://developers.google.com/youtube/v3/docs/videos/rate)
</details>

- <details><summary><code>get_rating</code></summary>
    <br>

    Get a video's rating.  
    **Required** parameters:
    - `video_id: str`

        The ID of the Video whose rating shall be retrieved.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`VideoGetRatingResponse`](#videogetratingresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/videos/getrating)
</details>

<!--m-end Video -->
<!--m-start Channel -->
#### `Channel`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a channel/list of channel resources.  
    **Required** parameters:
    - `part: ChannelPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `mine: bool`

        Specifies that the API should retrieve the channel of the authorised user.
    - `for_username: str`

        Specifies the name of the channel that should retrieve.
    - `id: str|list[str]`

        The ID of the channel to be retrieved.
    - `managed_by_me: bool`

        Specifies that the API should retrieve channels managed by the authenticated user.

    **Optional** parameters:
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ChannelListResponse`](#channellistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/channels/list)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a channel.  
    **Required** parameters:
    - `body: ChannelResource`

        The [`ChannelResource`](#channelresource) which specifies the details of the channel.  
        **Values you are able to set**:
        - `branding_settings.channel.description`
        - `branding_settings.channel.country`
        - `branding_settings.channel.default_language`
        - `branding_settings.channel.keywords`
        - `branding_settings.channel.moderate_comments`
        - `branding_settings.channel.tracking_analytics_account_id`
        - `branding_settings.channel.unsubscribed_trailer`
        - `status.self_declared_made_for_kids`
    - `part: ChannelPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ChannelResource`](#channelresource)

    [Reference](https://developers.google.com/youtube/v3/docs/channels/update)
</details>

<!--m-end Channel -->
<!--m-start ChannelSection -->
#### `ChannelSection`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of channel sections.  
    **Required** parameters:
    - `part: ChannelSectionPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `channel_id: str`

        Specifies a channel ID whose channel sections will be returned.
    - `id: str`

        The ID of the sections that should be retrieved.
    - `mine: bool`

        Specifies that the API should retrieve the channel section of the authorised user.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ChannelSectionListResponse`](#channelsectionlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Adds a channel section to the autheticated user's channel.  
    **Required** parameters:
    - `body: ChannelResource`

        The [`ChannelSectionResource`](#channelsectionresource) which specifies the details of the channel.  
        **Values you are able to set**:
        - `id`
        - `snippet.type`
        - `snippet.title`
        - `snippet.position`
        - `content_details.playlists`
        - `content_details.channels`
    - `part: ChannelSectionPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.
    - `on_behalf_of_content_owner_channel: str`

        Specifies the YouTube channel ID of the channel to which a video is being added.

    **Returns:** [`ChannelSectionResource`](#channelsectionresource)

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a channel section.  
    **Required** parameters:
    - `body: ChannelResource`

        The [`ChannelSectionResource`](#channelsectionresource) which specifies the details of the channel.  
        **Values you are able to set**:
        - `id`
        - `snippet.type`
        - `snippet.title`
        - `snippet.position`
        - `content_details.playlists`
        - `content_details.channels`
    - `part: ChannelSectionPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ChannelSectionResource`](#channelsectionresource)

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a channel section.  
    **Required** parameters:
    - `section_id: str`

        The ID of the channel section that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/delete)
</details>

<!--m-end ChannelSection -->
<!--m-start Search -->
#### `Search`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Searches something on youtube.  
    **Required** parameters:
    - `q: str`

        The query to search for.

    **Filters** (specify one or zero of these parameters.):
    - `for_content_owner: bool`

        Restricts the search to only retrieve videos owned by the content owner identified by the `on_behalf_of_content_owner` parameter.
    - `for_developer: bool`

        Restricts the search to only retrieve videos uploaded via the developer's application or website.
    - `for_mine: bool`

        Restricts the search to only retrieve videos owned by the authenticated user.
    - `related_to_video_id: bool`

        Specifies the ID of a video. The API will restrict the search result to videos related to that video.

    **Optional** parameters:
    - `order: Literal['date', 'rating', 'relevance', 'title', 'videoCount', 'viewCount']`

        Specifies the order of the resource.
    - `safe_search: Literal['none', 'moderate', 'strict']`

        Specifies whether the API should retrieve restricted content or not.
    - `type: Literal['channel', 'playlist', 'video']`

        Specifies what type of resource will be returned.
    - `published_after: str`

        Restricts the API to only return resources published after the specified time in the parameter.
    - `published_before: str`

        Restricts the API to only return resources published before the specified time in the parameter.
    - `region_code: str`

        Specifies to return search results available in the region code.
    - `relevance_language: str`

        Specifies to return search results that are most relevant to the specified language.
    - `location: str`

        Restricts the search result to resources published in the specified location.
        Used in conjunction with `location_radius`.
    - `location_radius: str`

        Specifies the area around the point provided by `location` to restrict videos.
    - `channel_id: str`

        Specifies that the result should only contain resources published by the provided channel.
    - `channel_type: Literal['show']`

        Restricts the search to a particular type of channel.
    - `event_type: Literal['completed', 'live', 'upcoming']`

        Restricts a search to broadcast events.
        Set the `type` parameter to `video` when specifying this parameter.
    - `video_caption: Literal['closedCaption', 'none']`

        See the attached reference.
    - `video_category_id: str`

        See the attached reference.
    - `video_definition: Literal['high', 'standard']`

        See the attached reference.
    - `video_dimension: Literal['2d', '3d']`

        See the attached reference.
    - `video_duration: Literal['long', 'medium', 'short']`

        See the attached reference.
    - `video_embeddable: Literal['true']`

        See the attached reference.
    - `video_license: Literal['creativeCommon', 'youtube']`

        See the attached reference.
    - `video_syndicated: Literal['true']`

        See the attached reference.
    - `video_type: Literal['episode', 'movie']`

        See the attached reference.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`SearchResultListResponse`](#searchresultlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/search/list)
</details>

<!--m-end Search -->
<!--m-start Subscription -->
#### `Subscription`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve subscription resources.  
    **Required** parameters:
    - `part: SubscriptionPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `channel_id: str`

        Specifies a channel ID whose subscriptions will be returned.
    - `id: str|list[str]`

        The ID of the channel to be retrieved.
    - `mine: bool`

        Specifies that the API should retrieve the subscriptions of the authorised user.
    - `my_recent_subscribers: bool`

        Retrieve a feed of the subscribers of the authenticated user in reverse chronological order.
    - `my_subscribers: bool`

        Retrieve a feed of the subscribers of the authenticated user in no particular order

    **Optional** parameters:
    - `order: Literal['alphabetical', 'relevance', 'unread']`

        Specifies the method that will be used to sort resources in the response.
    - `for_channel_id: str`

        Specifies a list of channel IDs, which the APi will only match to.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.
    - `on_behalf_of_content_owner_channel: str`

        Specifies the YouTube channel ID of the channel to which a video is being added.

    **Returns:** [`SubscriptionListResponse`](#subscriptionlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/subscriptions/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Subscribe to a channel.  
    **Required** parameters:
    - `channel_id: str`

        Specifies a channel ID to subscribe to.
    - `part: SubscriptionPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Returns:** [`SubscriptionResource`](#subscriptionresource)

    [Reference](https://developers.google.com/youtube/v3/docs/subscriptions/insert)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a subscription.  
    **Required** parameters:
    - `subscription_id: str`

        The ID of the subscription that will be deleted.

    [Reference](https://developers.google.com/youtube/v3/docs/subscriptions/delete)
</details>

<!--m-end Subscription -->

***
### Resources
This section describes the resources and responses used in the API. These classes are most often used in responses, as well as in methods that require a request body.  
Note that the attributes of these resources are in `snake_case`, not `camelCase` like in the original response. This is so as to follow the Python conventions.  
Also note that each resource has a `to_dict` method that returns the original response. That original response is a Python dictionary, and it's keys *will* be in `camelCase`. 

<!--r-start PlaylistResource -->
#### `PlaylistResource`

- <details><summary><code>PlaylistResource</code></summary>

</details>
<!--r-end PlaylistResource -->

<!--r-start PlaylistItemResource -->
#### `PlaylistItemResource`

- <details><summary><code>PlaylistItemResource</code></summary>

</details>
<!--r-end PlaylistItemResource -->

<!--r-start ThumbnailResource -->
#### `ThumbnailResource`

- <details><summary><code>ThumbnailResource</code></summary>

</details>
<!--r-end ThumbnailResource -->

<!--r-start CommentResource -->
#### `CommentResource`

- <details><summary><code>CommentResource</code></summary>

</details>
<!--r-end CommentResource -->

<!--r-start CommentThreadResource -->
#### `CommentThreadResource`

- <details><summary><code>CommentThreadResource</code></summary>

</details>
<!--r-end CommentThreadResource -->

<!--r-start I18nLanguageResource -->
#### `I18nLanguageResource`

- <details><summary><code>I18nLanguageResource</code></summary>

</details>
<!--r-end I18nLanguageResource -->

<!--r-start I18nRegionResource -->
#### `I18nRegionResource`

- <details><summary><code>I18nRegionResource</code></summary>

</details>
<!--r-end I18nRegionResource -->

<!--r-start VideoCategoryResource -->
#### `VideoCategoryResource`

- <details><summary><code>VideoCategoryResource</code></summary>

</details>
<!--r-end VideoCategoryResource -->

<!--r-start VideoAbuseReportReasonResource -->
#### `VideoAbuseReportReasonResource`

- <details><summary><code>VideoAbuseReportReasonResource</code></summary>

</details>
<!--r-end VideoAbuseReportReasonResource -->

<!--r-start VideoResource -->
#### `VideoResource`

- <details><summary><code>VideoResource</code></summary>

</details>
<!--r-end VideoResource -->

<!--r-start ChannelResource -->
#### `ChannelResource`

- <details><summary><code>ChannelResource</code></summary>

</details>
<!--r-end ChannelResource -->

<!--r-start ChannelSectionResource -->
#### `ChannelSectionResource`

- <details><summary><code>ChannelSectionResource</code></summary>

</details>
<!--r-end ChannelSectionResource -->

<!--r-start SearchResult -->
#### `SearchResult`

- <details><summary><code>SearchResult</code></summary>

</details>
<!--r-end SearchResult -->

<!--r-start SubscriptionResource -->
#### `SubscriptionResource`

- <details><summary><code>SubscriptionResource</code></summary>

</details>
<!--r-end SubscriptionResource -->

<!--r-start PlaylistListResponse -->
#### `PlaylistListResponse`

- <details><summary><code>PlaylistListResponse</code></summary>

</details>
<!--r-end PlaylistListResponse -->  

<!--r-start PlaylistItemListResponse -->
#### `PlaylistItemListResponse`

- <details><summary><code>PlaylistItemListResponse</code></summary>

</details>
<!--r-end PlaylistItemListResponse -->  

<!--r-start ThumbnailListResponse -->
#### `ThumbnailListResponse`

- <details><summary><code>ThumbnailListResponse</code></summary>

</details>
<!--r-end ThumbnailListResponse -->  

<!--r-start CommentListResponse -->
#### `CommentListResponse`

- <details><summary><code>CommentListResponse</code></summary>

</details>
<!--r-end CommentListResponse -->  

<!--r-start CommentThreadListResponse -->
#### `CommentThreadListResponse`

- <details><summary><code>CommentThreadListResponse</code></summary>

</details>
<!--r-end CommentThreadListResponse -->  

<!--r-start I18nLanguageListResponse -->
#### `I18nLanguageListResponse`

- <details><summary><code>I18nLanguageListResponse</code></summary>

</details>
<!--r-end I18nLanguageListResponse -->  

<!--r-start I18nRegionListResponse -->
#### `I18nRegionListResponse`

- <details><summary><code>I18nRegionListResponse</code></summary>

</details>
<!--r-end I18nRegionListResponse -->  

<!--r-start VideoCategoryListResponse -->
#### `VideoCategoryListResponse`

- <details><summary><code>VideoCategoryListResponse</code></summary>

</details>
<!--r-end VideoCategoryListResponse -->  

<!--r-start VideoAbuseReportReasonListResponse -->
#### `VideoAbuseReportReasonListResponse`

- <details><summary><code>VideoAbuseReportReasonListResponse</code></summary>

</details>
<!--r-end VideoAbuseReportReasonListResponse -->  

<!--r-start VideoListResponse -->
#### `VideoListResponse`

- <details><summary><code>VideoListResponse</code></summary>

</details>
<!--r-end VideoListResponse -->  

<!--r-start ChannelListResponse -->
#### `ChannelListResponse`

- <details><summary><code>ChannelListResponse</code></summary>

</details>
<!--r-end ChannelListResponse -->  

<!--r-start ChannelSectionListResponse -->
#### `ChannelSectionListResponse`

- <details><summary><code>ChannelSectionListResponse</code></summary>

</details>
<!--r-end ChannelSectionListResponse -->  

<!--r-start SearchListResponse -->
#### `SearchListResponse`

- <details><summary><code>SearchListResponse</code></summary>

</details>
<!--r-end SearchListResponse -->  

<!--r-start SubscriptionListResponse -->
#### `SubscriptionListResponse`

- <details><summary><code>SubscriptionListResponse</code></summary>

</details>
<!--r-end SubscriptionListResponse -->  
